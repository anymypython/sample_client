import requests
from config import settings
from src.plugins import get_server_info
import json


class BaseHandler(object):
    """
    基类, 定义需要重新的方法
    """

    def cmd(self, command, hostname=None):
        raise NotImplementedError("cmd() must be Implemented")

    def handler(self):
        raise NotImplementedError("handler() must be Implemented")


class SSHandSaltHandler(object):
    """
    SSH和salt模式基类
    """

    def handler(self):
        """
        获取资产,提报获取结果
        :return: 
        """
        r1 = requests.get(url=settings.HOST_ASSET_API)
        host_list = r1.json()
        print(host_list)
        from concurrent.futures import ThreadPoolExecutor
        pool = ThreadPoolExecutor(10)
        for hostname in host_list:
            """循环主机列表, 提交异步提交任务"""
            pool.submit(self.task(hostname))

    def task(self, hostname):
        # 采集资产
        info = get_server_info(self, hostname)
        # 上报采集结果
        r2 = requests.post(url=settings.HOST_ASSET_API,
                           data=json.dumps(info),  # url编码a=1&b=2 ,直接用不方便
                           headers={'Content-Type': 'application/json'}
                           )
