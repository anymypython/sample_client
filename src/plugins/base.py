from config import settings


class BasePlugin:
    # 硬件基本配置
    def __init__(self):
        self.debug = settings.DEBUG
        self.base_dir = settings.BASE_DIR
        # 初始化获取调试模式, 根目录

    def get_os(self, handler, hostname):
        # os = handler.cmd("查询操作系统的命令", hostname)
        return "win32"

    def process(self, handler, hostname):
        # 选择平台执行相应的方法
        os_what = self.get_os(handler, hostname)
        if os_what == "win32":
            return self.win(handler, hostname)
        else:
            return self.linux(handler, hostname)

    def win(self, handler, hostname):
        raise NotImplementedError('win() must Implemented ')

    def linux(self, handler, hostname):
        raise NotImplementedError('linux() must Implemented ')
