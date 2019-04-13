from .base import SSHandSaltHandler


class SaltHandler(SSHandSaltHandler):
    def cmd(self, command, hostname=None):
        """
        调用saltstack远程连接主机并执行命令(saltstack的master)
        :param command: 要执行的命令
        :param hostname: 主机名
        :return:
        """
        import salt.clent
        local = salt.clent.LocalClient()  # 实例化一个salt连接
        result = local.cmd(hostname, "cmd.run", [command])  # 执行请求命令 ,获取结果
        return result[hostname]
