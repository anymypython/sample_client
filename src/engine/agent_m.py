from .base import BaseHandler
from src.plugins import get_server_info
from config import settings
import json
import requests
import os


class AgentHandler(BaseHandler):
    """
    agent模式操作引擎
    """

    def cmd(self, command, hostname=None):
        """
        执行命令, 获取命令的结果
        :param command: 获取信息的命令
        :param hostname: 主机名
        :return:  返回获取结果
        """
        import subprocess
        return subprocess.getoutput(command)

    def handler(self):
        """
        调用此方法: 执行操作, 获取信息,解析, 发送请求上报结果
        :return: 
        """
        print("agent模式")
        # 采集资产信息: 硬盘, 内存, 网卡
        info = get_server_info(self)
        # 唯一标识: 判断采集信息是否第一次提交        
        if not os.path.exists(settings.CERT_FILE_PATH):
            info["type"] = "create"  # 新增       
        else:
            # 主机信息文件存在, 读取
            with open(settings.CERT_FILE_PATH, "r", encoding="utf-8") as f:
                cert = f.read()
                hostname = info["basic"]["data"]["hostname"]
                print(cert)
                print(hostname)
                if cert == hostname:  # 文件保存的主机名与本地监测到的相同
                    info["type"] = "update"
                else:
                    # 主机名变更过, 更新资产信息
                    info["type"] = "host_update"
                    info["cert"] = cert
        # 3上报给api
        r1 = requests.post(url="http://127.0.0.1:8000/api/asset", data=json.dumps(info),
                           headers={'Content-Type': 'application/json'})
        print(r1)
        print(r1.text)
        # 4 更新唯一标识
        response = re.json
        if response.get("status"):
            """
            是否修改主机名
            """
            with open("settings.CERT_FILE_PATH", "w", encoding="utf-8") as f:
                f.write(response["data"])
                print("update host")

        print("end")
