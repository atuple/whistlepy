class BaseWhistleAPI(object):
    """ Whistle API base class """

    API_PATH_URL = ""

    def __init__(self, client):
        self._client = client

    def _get(self, url, **kwargs):
        if getattr(self, 'API_BASE_URL', None):
            kwargs['api_base_url'] = self.API_BASE_URL

        return self._client.get(self.API_PATH_URL + url, **kwargs)

    def _post(self, url, **kwargs):
        if getattr(self, 'API_BASE_URL', None):
            kwargs['api_base_url'] = self.API_BASE_URL
        return self._client.post(self.API_PATH_URL + url, **kwargs)

    @property
    def _access_token(self):
        return self._client.access_token

    @property
    def session(self):
        return self._client.session

    @property
    def appkey(self):
        return self._client.appkey
