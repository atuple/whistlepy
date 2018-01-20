from whistlepy.client.api.base import BaseWhistleAPI


class WhistleOAuthApi(BaseWhistleAPI):

    API_PATH_URL = "api/v2/index.php/user/"

    def auth_user(self, verify):
        """
        根据 verify 验证用户身份
        详情请参考
        http://open.weishao.com.cn/doc/api#yzyh

        :param verify: 通过成员授权获取到的verify
        :param access_token: access_token
        :return: 返回的 JSON 数据包
        """

        return self._get(
            'authUser',
            params={
                'verify': verify,
                'access_token': self._access_token
            }
        )

    def get_user_info(self, student_number):
        """
        根据 student_number 获取用户信息
        详情请参考
        http://open.weishao.com.cn/doc/api#hvyhxx

        :param student_number: 通过成员授权获取到的student_number
        :return: 返回的 JSON 数据包
        """
        return self._get(
            'getInfo',
            params={
                'student_number': student_number,
                'access_token': self._access_token
            }
        )
