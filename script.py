# import requests
# import json
#
#
# def agent():
#     info = {"hostname": "c1.com", "memory": "kis2G", "author": "黎明"}
#     # res = requests.post(url="http://127.0.0.1:8000/api/asset", json=info)
#     ret = requests.post(url="http://127.0.0.1:8000/api/asset", data=json.dumps(info))
#     # print(res)
#     # print(res.text)
#     print(ret)
#
#
# # agent()
# def get_host():
#     ret = requests.get(url="http://127.0.0.1:8000/api/asset")
#     print(ret.text)
#
#
# import sys
#
# print(sys.path)
# agent()
# get_host()

# import redis
#
# r = redis.Redis(host="192.168.15.107", port=6666)
# res = r.set("alex", 39)
# print(res)