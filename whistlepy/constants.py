from enum import Enum

class WhistleErrorCode(Enum):
    """
    微哨接口返回码，全局返回码请参考 http://open.weishao.com.cn/doc/api
    """

    成功 = 1000
    用户未登陆 = 1001
    用户verify不正确 = 1002
    app_key错误或应用未上架 = 1003
    参数不全 = 1004
    用户为订阅该该应用不能向其发送通知 = 1005
    所查信息不存在 = 1006
    未知的消息类型 = 1007
    消息格式错误 = 1008
    节点拥有子节点不能删除 = 1009
    标题过长 = 1010
    消息内容过长 = 1011
    数据已存在 = 1012
    时间格式不对或者定时时间已过 = 1013
    参数domain错误domain不存在 = 1014
    获取学校消息错误= 1015
    ldap服务器连接失败 = 1016
    用户名或密码错 = 1017
    用户已被禁用 = 1018
    oauth服务异常 = 1019
    用户数量大于限定值 = 1020
    学校未开通定位功能 = 2001
    所查位置节点不存在 = 2002
    学号不存在 = 2002
    所查信息不存在哦 = 2003
