from whistlepy.client.api.base import BaseWhistleAPI


class WhistleAdhocApi(BaseWhistleAPI):
    API_PATH_URL = "api/v2/index.php/adhoc/"

    def get_list(self):
        """
        非常设机构接口.

        详情请参考
        http://open.weishao.com.cn/doc/api#zzs

        :return: 返回的 JSON 数据包
        """

        return self._get(
            'getList',
            params={
                'access_token': self._access_token
            }
        )