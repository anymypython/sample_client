import os
import traceback
from .base import BasePlugin
from lib.response import BaseResponse
from lib.log import logger


class MainBoard(BasePlugin):
    def win(self, handler, hostname):
        response = BaseResponse()
        return response.dict

    def linux(self, handler, hostname):
        response = BaseResponse()
        try:
            if self.debug:
                from config.settings import BASE_DIR
                with open(os.path.join(BASE_DIR, 'files', 'board.out'), 'r') as f:
                    output = f.read()
            else:
                shell_command = "sudo dmidecode -t1"
                output = handler.cmd(shell_command, hostname)
            response.data = self.parse(output)
        except Exception as e:
            msg = traceback.format_exc()
            response.status = False
            response.error = msg
            logger.error(msg)
        return response.dict

    def parse(self, conntent):
        result = {}
        key_map = {
            'Manufacturer': 'manufacturer',
            'Product Name': 'model',
            'Serial Number': 'sn',
        }
        for item in content.split('\n'):
            row_data = item.strip().split(':')
            if len(row_data) == 2:
                if row_data[0] in key_map:
                    result[key_map[row_data[0]]] = row_data[1].strip() if row_data[1] else row_data[1]

        return result
