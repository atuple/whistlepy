from whistlepy.client.api.base import BaseWhistleAPI


class WhistleAuthApi(BaseWhistleAPI):

    API_PATH_URL = "api/v2/index.php/auth/"

    def add_auth(self, school, auth_detail):
        """
        新建权限

        第三方应用通过本接口可以在给定学校的组织树、标签、非常设机构中选择部分或全部人群，生成一个权限的范围，用于有人员限定相关的应用场景。
        详情请参考
        http://open.weishao.com.cn/doc/api

        :param school: 学校标识
        :param auth_detail: 权限范围，其数据内容参见参数示例，需要将JSON转为字符串表示
        :param access_token: access_token
        :return: 返回的 JSON 数据包
        """

        return self._post(
            'addAuth',
            params={
                'school': school,
                'auth_detail': auth_detail,
                'access_token': self._access_token
            }
        )

    def get_auth(self, school, authority_id):
        """
        查询权限范围
        第三方应用通过本接口可以查询由本应用添加的权限范围信息。
        http://open.weishao.com.cn/doc/api#hvyhxx

        :param school: 学校标识
        :param authority_id: 权限ID
        :return: 返回的 JSON 数据包
        """
        return self._get(
            'getAuth',
            params={
                'school': school,
                'authority_id': authority_id,
                'access_token': self._access_token
            }
        )

    def edit_auth(self, school, authority_id, auth_detail):
        """
        编辑权限范围
        第三方应用通过本接口可以编辑由本应用添加的权限范围。
        http://open.weishao.com.cn/doc/api#hvyhxx

        :param school: 学校标识
        :param authority_id: 权限ID
        :param auth_detail 权限范围，其数据内容参见参数示例，需要将JSON转为字符串表示

        :return: 返回的 JSON 数据包
        """
        return self._post(
            'EditAuth',
            params={
                'school': school,
                'authority_id': authority_id,
                'auth_detail': auth_detail,
                'access_token': self._access_token
            }
        )

