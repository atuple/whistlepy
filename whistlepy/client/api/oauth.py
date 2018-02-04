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

    def search_global_user_list(self, name, search_flag="all", status=1, page=1, count=20):
        """
        第三方应用服务器通过本方法可以查询给定学工号对应的用户基本信息.
        详情请参考
        http://open.weishao.com.cn/doc/api#yhssjk

        :param name: 用户姓名或者拼音 或者学号
        :param status: 用户状态，取值为0 或1,0为禁用
        :param search_flag: 默认为all表示搜索姓名 拼音和学号，取其他值则只搜索姓名
        :param page: 页码
        :param count: 单页数量
        :return: 返回的 JSON 数据包
        """
        return self._get(
            'searchGlobalUserList',
            params={
                'name': name,
                'status': status,
                'search_flag': search_flag,
                'page': page,
                'count': count,
                'access_token': self._access_token
            }
        )
