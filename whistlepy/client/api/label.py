from whistlepy.client.api.base import BaseWhistleAPI


class WhistleLabelApi(BaseWhistleAPI):
    API_PATH_URL = "api/v2/index.php/label/"

    def get_list(self):
        """
        第三方应用服务器通过本方法可以查询学校已创建的标签，与获取用户信息接口配合使用，可以区分不同身份属性的用户。

        详情请参考
        http://open.weishao.com.cn/doc/api#bqlbxyhlb

        :param organization_id 组织节点id,可通过查询0节点找到学校的根节点信息

        :return: 返回的 JSON 数据包
        """

        return self._get(
            'getList',
            params={
                'access_token': self._access_token
            }
        )

    def get_user_list(self, label_id, offset=None, pagesize=None):
        """
        第三方应用服务器通过本方法可以查询学校某标签下的用户列表。

        详情请参考
        http://open.weishao.com.cn/doc/api#bqlbxyhlb

        :param label_id 标签id
        :param offset   起始位置，为空时从第一条开始取(非必填)
        :param pagesize 单次返回结果数量，为空时取至最后一条（非必填）

        :return: 返回的 JSON 数据包
        """
        params = {
            'label_id': label_id,
            'access_token': self._access_token
        }

        if offset:
            params["offset"] = offset

        if pagesize:
            params["pagesize"] = pagesize

        return self._get(
            'getUserList',
            params=params
        )
