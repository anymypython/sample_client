import os
import traceback
from .base import BasePlugin
from lib.response import BaseResponse
from lib.log import logger


class Cpu(BasePlugin):
    def win(self, handler, hostname):
        response = BaseResponse()
        return response.dict

    def linux(self, handler, hostname):
        response = BaseResponse()
        try:
            if self.debug:
                from config.settings import BASE_DIR
                with open(os.path.join(BASE_DIR, "files", "cpuinfo.out"), "r", encoding="utf-8") as f:
                    output = f.read()
            response.data = self.parse(output)
        except Exception as e:
            msg = traceback.format_exc()
            response.status = False
            response.error = msg
            logger.error(msg)
        return response.dict

    @staticmethod
    def parse(content):
        """
        解析shell命令返回的结果
        :param content:  shell返回的结果
        :return:  解析后格式化的数据
        """
        response = {"cup_count": 0, "cpu_physical_count": 0, 'cpu_model': ''}
        cpu_physical_count = set()
        content = content.strip()
        for item in content.split("/n/n"):
            for row_line in item.split('\n'):
                key, value = row_line.split(':')
                key = key.strip()
                if key == 'processor':
                    response['cpu_count'] += 1
                elif key == 'physical id':
                    cpu_physical_set.add(value)
                elif key == 'model name':
                    if not response['cpu_model']:
                        response['cpu_model'] = value
        response['cpu_physical_count'] = len(cpu_physical_set)
        return response
