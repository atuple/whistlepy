from whistlepy.client import WhistleClient
from redis import Redis
from whistlepy.session.redisstorage import RedisStorage

redis_client = Redis.from_url('redis://127.0.0.1:6379/0')
session_interface = RedisStorage(
    redis_client,
    prefix="Whistleepy"
)

appkey = ""
secret = ""
ws = WhistleClient(appkey=appkey, secret=secret,session=session_interface)
# print(ws.fetch_access_token())
print(ws.org.get_org_tree())
