from whistlepy.client.api.base import BaseWhistleAPI


class WhistleNotificationApi(BaseWhistleAPI):
    API_PATH_URL = "api/v2/index.php/notification/"

    def get_list(self):
        """
        第三方应用服务器通过本方法可以查询本应用已经发送过的通知记录.

        详情请参考
        http://open.weishao.com.cn/doc/api#yzyh

        :return: 返回的 JSON 数据包
        """

        return self._get(
            'getList',
            params={
                'access_token': self._access_token
            }
        )

    def get_detail(self, notification_id):
        """
        第三方应用服务器通过本方法可以查询指定通知记录的详情.

        详情请参考
        http://open.weishao.com.cn/doc/api#hvyhxx

        :param notification_id 通知的id
        :return: 返回的 JSON 数据包
        """
        return self._get(
            'getDetails',
            params={
                'notification_id': notification_id,
                'access_token': self._access_token
            }
        )

    def send_notification(self, notification_data):
        """
        第三方应用服务器通过本方法可以发送通知.

        详情请参考
        http://open.weishao.com.cn/doc/api#fstz

        :param notification_data  {type: sendList: .......}
        :return: 返回的 JSON 数据包(notification_id)
        """
        notification_data["access_token"] = self._access_token
        print(notification_data)
        return self._post(
            'sendNotification?access_token=' + self._access_token,
            params=notification_data
        )