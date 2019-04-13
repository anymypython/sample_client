import traceback
from .base import BasePlugin
from lib.response import BaseResponse
from lib.log import logger


class Basic(BasePlugin):
    def os_platform(self, handler, hostname):
        """
        获取系统平台
        :param handler: 
        :param hostname: 
        :return: 
        """
        output = handler.cmd("uname", hostname)
        return output.strip()

    def os_version(self, handler, hostname):
        """获取系统版本"""
        output = handler.cmd("cat /etc/issue", hostname)
        result = output.strip().split("\n")[0]
        return result

    def os_hostname(self, handler, hostname):
        """获取主机名"""
        output = handler.cmd("hostname", hostname)
        return output.strip

    def win(self, handler, hostname):
        response = BaseResponse()
        return response.dict

    def linux(self, handler, hostname):
        response = BaseResponse()  # 相应对象
        try:
            if self.debug:
                ret = {
                    "os_platform": "linux",
                    "os_version": "6.5",
                    "hostname": "c2.com"
                }
            else:
                ret = {
                    "os_platform": self.os_platform(handler, hostname),
                    "os_version": self.os_version(handler, hostname),
                    "hostname": self.os_hostname(handler, hostname)
                }
            response.data = ret
        except Exception as e:
            msg = traceback.format_exc()
            response.status = False
            response.error = msg
            logger.error(msg)

        return response.dict
