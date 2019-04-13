from config import settings
from lib.moduler_string import import_string


def get_server_info(handler, hostname=None):
    """
    获取所有资产的信息并返回
    :param handler:
    :param hostname:
    :return:
    """
    info = {}
    for name, path in settings.PLUGINS_DICT.items():
        """
        'disk': 'src.plugins.disk.Disk',
        'memory': 'src.plugins.memory.Memory',
        'network': 'src.plugins.network.Network',
        """
        cls = import_string((path))
        obj = cls()
        info[name] = obj.process(handler, hostname)
    return info
