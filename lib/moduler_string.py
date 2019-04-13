import importlib


def import_string(path):
    """
    模块导入
    :param path: 模块所在文件 
    :return: 返回一个引擎类
    """
    # "src.plugins.disk.Disk"
    moduler_path, engine_class = path.rsplit(".", maxsplit=1)
    module = importlib.import_module(moduler_path)
    return getattr(module, engine_class)
