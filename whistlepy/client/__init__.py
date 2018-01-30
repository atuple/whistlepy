from whistlepy.client.base import BaseWhistleClient
from whistlepy.client import api


class WhistleClient(BaseWhistleClient):
    """
    微信 API 操作类
    通过这个类可以操作微信 API，发送主动消息、群发消息和创建自定义菜单等。
    """

    API_BASE_URL = 'https://api.weishao.com.cn/'

    def __init__(self, appkey, secret, access_token=None,
                 session=None, timeout=None, auto_retry=True, scope="all"):
        super(WhistleClient, self).__init__(
            appkey, access_token, session, timeout, auto_retry
        )
        self.appkey = appkey
        self.secret = secret
        self.scope = scope
        # 插件
        self.oauth = api.WhistleOAuthApi(self)
        self.notification = api.WhistleNotificationApi(self)
        self.org = api.WhistleOrganizationApi(self)
        self.label = api.WhistleLabelApi(self)
        self.geo = api.WhistleWifiLocApi(self)
        self.adhoc = api.WhistleAdhocApi(self)

    def fetch_access_token(self):
        """
        获取/刷新 access token
        详情请参考 http://open.weishao.com.cn/doc/api#hqtoken
        :return: 返回的 JSON 数据包
        """
        return self._fetch_access_token(
            url='https://api.weishao.com.cn/oauth/token',
            data={
                'grant_type': 'client_credentials',
                'app_key': self.appkey,
                'app_secret': self.secret,
                'scope': self.scope
            }
        )
