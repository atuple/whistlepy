微哨(Whistle) 第三方 Python SDK。

作者 sai

## 功能特性
 1. 支持 py3/pypy3
 2. 支持 进程内存，memcached, redis 作为缓存
 3. 插件化设计, 方便添加新接口
 
 
## 未来
 1. 多实例缓存，方便SAAS应用构建
 2. 更多的非官方功能接口
 
## 实现接口

1. 基础接口

    获取access_token
    
    刷新access_token
    
2. 用户接口

    验证用户身份

    获取用户信息
    
3. 通知接口

    获取已发送通知列表
    
    获取通知详情
    
    发送通知

5. 通讯录接口

    获取组织节点树下的所有用户信息
    
    获取学校的标签列表
    
    获取标签下用户列表
    
    获取非常用机构列表

6. 无线定位接口

    获取所有位置的相关信息
    
    获取位置节点下当前的用户列表
    
    批量查询用户的当前位置
    
    查询用户的历史轨迹
    
    用户位置变化实时推送

7. 积分接口

    应用增加积分
    
    应用消费积分

8. 权限接口

    新建权限
    
    查询权限范围

    编辑权限范围
    
9. 岗位接口

    岗位列表
    
    获取岗位详情


pip 安装
```bash
pip install whistlepy
```


## 使用示例

```bash
from whistlepy.client import WhistleClient

appkey = "appkey"
secret = "secret"
ws = WhistleClient(appkey=appkey, secret=secret)
print(ws.access_token)
print(ws.oauth.get_user_info("student_number"))

```

