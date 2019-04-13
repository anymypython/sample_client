from .base import SSHandSaltHandler

from config import settings


class SSHHandler(SSHandSaltHandler):
    def cmd(self, command, hostname=None):
        import paramiko
        # 连接客户端主机私钥
        private_key = paramiko.RSAKey.from_private_key_file(settings.SSH_PRIVATE_KEY)
        # 生成ssh客户端
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)  # 自动协商连接的密钥类型
        # 连接主机
        ssh.connect(hostname=hostname, port=settings.SSH_PORT, username=settings.SSH_USER, pkey=private_key)
        # 执行命令,获取执行结果
        stdin, stdout, stderr = ssh.exec_command(command)
        result = stdout.read()  # 读取执行结果标准输出
        ssh.close()  # 关闭连接
        return result  # 返回结果
