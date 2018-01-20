from whistlepy.utils import to_binary, to_text


class WhistleException(Exception):
    """Base exception for Whistlepy"""

    def __init__(self, errcode, errmsg):
        """
        :param errcode: Error code
        :param errmsg: Error message
        """
        self.errcode = errcode
        self.errmsg = errmsg

    def __str__(self):
        _repr = 'Error code: {code}, message: {msg}'.format(
            code=self.errcode,
            msg=self.errmsg
        )

        return to_text(_repr)

    def __repr__(self):
        _repr = '{klass}({code}, {msg})'.format(
            klass=self.__class__.__name__,
            code=self.errcode,
            msg=self.errmsg
        )

        return to_text(_repr)


class WhistleClientException(WhistleException):
    """Whistle API client exception class"""
    def __init__(self, errcode, errmsg, client=None,
                 request=None, response=None):
        super(WhistleClientException, self).__init__(errcode, errmsg)
        self.client = client
        self.request = request
        self.response = response


class InvalidSignatureException(WhistleException):
    """Invalid signature exception class"""

    def __init__(self, errcode=-40001, errmsg='Invalid signature'):
        super(InvalidSignatureException, self).__init__(errcode, errmsg)


class APILimitedException(WhistleClientException):
    """Whistle API call limited exception class"""
    pass


class InvalidAppIdException(WhistleException):
    """Invalid app_id exception class"""

    def __init__(self, errcode=-40005, errmsg='Invalid AppId'):
        super(InvalidAppIdException, self).__init__(errcode, errmsg)


class WhistleOAuthException(WhistleClientException):
    """Whistle OAuth API exception class"""
    pass

