from whistlepy.client.api.base import BaseWhistleAPI


class WhistleOrganizationApi(BaseWhistleAPI):
    API_PATH_URL = "api/v2/index.php/organization/"

    def get_org_tree(self, organization_id=0):
        """
        第三方应用服务器通过本方法可以查询给定组织节点下对应的组织信息和成员构成(但不递归子组织节点).

        详情请参考
        http://open.weishao.com.cn/doc/api#zzs

        :param organization_id 组织节点id,可通过查询0节点找到学校的根节点信息
        :param access_token: access_token
        :return: 返回的 JSON 数据包
        """

        return self._get(
            'getOrgTree',
            params={
                'organization_id': organization_id,
                'access_token': self._access_token
            }
        )