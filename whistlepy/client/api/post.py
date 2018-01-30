from whistlepy.client.api.base import BaseWhistleAPI


class WhistlePostApi(BaseWhistleAPI):
    API_PATH_URL = "api/v2/index.php/post/"
    API_BASE_URL = "https://k12.api.weishao.com.cn/"

    def get_list(self):
        """
        岗位列表

        第三方应用服务器通过本方法获取学校的岗位列表。

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

    def get_detail(self, post_id=None, student_number=None, organization_id=None):
        """
        获取岗位详情
        第三方应用服务器通过本方法获取学校的岗位详情,如果参数不传的话，会全量返回所有岗位信息。

        详情请参考
        http://open.weishao.com.cn/doc/api#zzs

        :return: 返回的 JSON 数据包
        """
        params = {'access_token': self._access_token}
        if post_id:
            params["post_id"] = post_id
        if student_number:
            params["student_number"] = student_number
        if organization_id:
            params["organization_id"] = organization_id

        return self._get(
            'getDetailList',
            params=params
        )
