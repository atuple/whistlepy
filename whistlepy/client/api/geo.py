from whistlepy.client.api.base import BaseWhistleAPI


class WhistleWifiLocApi(BaseWhistleAPI):
    API_PATH_URL = "api/v2/index.php"

    def get_loc_info(self):
        """
        第三方应用服务器通过本方法可以获取在定位引擎中配置的所有位置的信息。

        详情请参考
        http://open.weishao.com.cn/doc/api#bqlbxyhlb

        :return: 返回的 JSON 数据包
        """

        return self._get(
            '',
            params={
                'm': "wifiloc",
                'a': "getLocInfo",
                'access_token': self._access_token
            }
        )

    def get_user_list(self, poiList):
        """
        第三方应用服务器通过本方法可以获取在某些位置节点下目前所有用户的信息。

        详情请参考
        http://open.weishao.com.cn/doc/api#bqlbxyhlb

        :param poiList 查询位置的poiid。

        :return: 返回的 JSON 数据包
        """

        return self._post(
            '?m=wifiloc&a=getUserList&access_token=' + self._access_token,
            params={
                'poiList': poiList,
                'access_token': self._access_token
            }
        )

    def get_user_loc(self, userList):
        """
        第三方应用服务器通过本方法可以查询某些用户的当前位置。

        详情请参考
        http://open.weishao.com.cn/doc/api#bqlbxyhlb

        :param userList ["1", "2", "3"] //用户学工号的列表。

        :return: 返回的 JSON 数据包
        """

        return self._post(
            '?m=wifiloc&a=getUsersLoc&access_token=' + self._access_token,
            params={
                'userList': userList,
                'access_token': self._access_token
            }
        )

    def get_user_loc_hist(self, student_number, start_ts=None,end_ts=None):
        """
        第三方应用服务器通过本方法可以查询某个用户的历史轨迹，目前支持7天内轨迹查询。

        详情请参考
        http://open.weishao.com.cn/doc/api#bqlbxyhlb

        :param student_number 用户的学工号
        :param start_ts       查询轨迹的起始unix时间戳，默认为当前时刻时间戳
        :param end_ts         查询轨迹的结束unix时间戳，默认为当前时刻时间戳

        :return: 返回的 JSON 数据包
        """
        params = {
            'm': "wifiloc",
            'a': "getUserLocHist",
            'student_number': student_number,
            'access_token': self._access_token
        }
        if start_ts:
            params["start_ts"] = start_ts

        if end_ts:
            params["end_ts"] = end_ts

        return self._get(
            '',
            params=params
        )

    def set_push_callback(self, callback_url):
        """
        第三方应用服务器如果需要使用位置变化实时推送接口，首先设置服务器回调接口url，
        当订阅该应用的用户位置发生变化时，将会同POST请求方式把实时位置发送到该url。

        详情请参考
        http://open.weishao.com.cn/doc/api#bqlbxyhlb

        :param callback_url 回调接口的url，参数务必进行url encode

        :return: 返回的 JSON 数据包
        """

        return self._get(
            '',
            params={
                'm': "wifiloc",
                'a': "setPushCallback",
                'callback_url': callback_url,
                'access_token': self._access_token
            }
        )
