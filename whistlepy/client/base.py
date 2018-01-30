import time
import inspect
import logging
import warnings

import six
import requests

from whistlepy.utils import json, get_querystring
from whistlepy.session.memorystorage import MemoryStorage
from whistlepy.exceptions import WhistleClientException, APILimitedException
from whistlepy.client.api.base import BaseWhistleAPI


logger = logging.getLogger(__name__)


def _is_api_endpoint(obj):
    return isinstance(obj, BaseWhistleAPI)


class BaseWhistleClient(object):

    _http = requests.Session()

    API_BASE_URL = ''

    def __new__(cls, *args, **kwargs):
        self = super(BaseWhistleClient, cls).__new__(cls)
        api_endpoints = inspect.getmembers(self, _is_api_endpoint)
        for name, api in api_endpoints:
            api_cls = type(api)
            api = api_cls(self)
            setattr(self, name, api)
        return self

    def __init__(self, appkey, access_token=None, session=None, timeout=None, auto_retry=True):
        self.appkey = appkey
        self.expires_at = None
        self.session = session or MemoryStorage()
        self.timeout = timeout
        self.auto_retry = auto_retry

        if isinstance(session, six.string_types):
            from shove import Shove
            from whistlepy.session.shovestorage import ShoveStorage

            querystring = get_querystring(session)
            prefix = querystring.get('prefix', ['Whistlepy'])[0]

            shove = Shove(session)
            storage = ShoveStorage(shove, prefix)
            self.session = storage

        if access_token:
            self.session.set(self.access_token_key, access_token)

    @property
    def access_token_key(self):
        return '{0}_access_token'.format(self.appkey)

    def _request(self, method, url_or_endpoint, **kwargs):
        if not url_or_endpoint.startswith(('http://', 'https://')):
            api_base_url = kwargs.pop('api_base_url', self.API_BASE_URL)
            url = '{base}{endpoint}'.format(
                base=api_base_url,
                endpoint=url_or_endpoint
            )
        else:
            url = url_or_endpoint

        if 'params' not in kwargs:
            kwargs['params'] = {}
        if isinstance(kwargs['params'], dict) and \
                'access_token' not in kwargs['params']:
            kwargs['params']['access_token'] = self.access_token
        if isinstance(kwargs.get('data', ''), dict):
            body = json.dumps(kwargs['data'], ensure_ascii=False)
            body = body.encode('utf-8')
            kwargs['data'] = body

        if method.lower() == "post":
            kwargs['json'] = kwargs['params']
            del kwargs['params']

        kwargs['timeout'] = kwargs.get('timeout', self.timeout)
        result_processor = kwargs.pop('result_processor', None)
        res = self._http.request(
            method=method,
            url=url,
            **kwargs
        )
        return self._handle_result(
            res, method, url, result_processor, **kwargs
        )

    def _decode_result(self, res):
        try:
            result = json.loads(res.content.decode('utf-8', 'ignore'), strict=False)
        except (TypeError, ValueError):
            # Return origin response object if we can not decode it as JSON
            logger.debug('Can not decode response as JSON', exc_info=True)
            return res
        return result

    def _handle_result(self, res, method=None, url=None,
                       result_processor=None, **kwargs):
        if not isinstance(res, dict):
            # Dirty hack around asyncio based AsyncWhistleClient
            result = self._decode_result(res)
        else:
            result = res

        if not isinstance(result, dict):
            return result

        if 'errcode' in result:
            result['errcode'] = int(result['errcode'])

        if 'code' in result and result["code"] == 401:
            if result['errno'] == 100401:
                print("access_token  errors")

        if 'errcode' in result and result['errcode'] != 1000:
            errcode = result['errcode']
            errmsg = result.get('errmsg', errcode)
            if self.auto_retry and errcode in []:
                logger.info('Access token expired, fetch a new one and retry request')
                self.fetch_access_token()
                access_token = self.session.get(self.access_token_key)
                kwargs['params']['access_token'] = access_token
                return self._request(
                    method=method,
                    url_or_endpoint=url,
                    result_processor=result_processor,
                    **kwargs
                )

        return result if not result_processor else result_processor(result)

    def get(self, url, **kwargs):
        return self._request(
            method='get',
            url_or_endpoint=url,
            **kwargs
        )

    def _get(self, url, **kwargs):
        warnings.warn('`_get` method of `WhistleClient` is deprecated, will be removed in 1.6,'
                      'Use `get` instead',
                      DeprecationWarning, stacklevel=2)
        return self.get(url, **kwargs)

    def post(self, url, **kwargs):
        return self._request(
            method='post',
            url_or_endpoint=url,
            **kwargs
        )

    def _post(self, url, **kwargs):
        warnings.warn('`_post` method of `WhistleClient` is deprecated, will be removed in 1.6,'
                      'Use `post` instead',
                      DeprecationWarning, stacklevel=2)
        return self.post(url, **kwargs)

    def _fetch_access_token(self, url, data):
        """ The real fetch access token """
        logger.info('Fetching access token')
        res = self._http.post(
            url=url,
            json=data
        )
        try:
            res.raise_for_status()
        except requests.RequestException as reqe:
            raise WhistleClientException(
                errcode=None,
                errmsg=None,
                client=self,
                request=reqe.request,
                response=reqe.response
            )
        result = res.json()
        if 'errcode' in result and result['errcode'] != 0:
            raise WhistleClientException(
                result['errcode'],
                result['errmsg'],
                client=self,
                request=res.request,
                response=res
            )

        expires_in = 7200
        if 'expires_in' in result:
            expires_in = result['expires_in']
        self.session.set(
            self.access_token_key,
            result['access_token'],
            expires_in
        )
        self.expires_at = int(time.time()) + expires_in
        return result

    def fetch_access_token(self):
        raise NotImplementedError()

    @property
    def access_token(self):
        """ Whistle access token """
        access_token = self.session.get(self.access_token_key)
        if access_token:
            if not self.expires_at:
                # user provided access_token, just return it
                return access_token

            timestamp = time.time()
            if self.expires_at - timestamp > 60:
                return access_token

        self.fetch_access_token()
        return self.session.get(self.access_token_key)
