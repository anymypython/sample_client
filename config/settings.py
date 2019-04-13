import os

# 全局配置文件
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # 项目根目录
# 客户端获取资产模式aget/ssh/salt
ENGINE = "agent"
# 引擎实例类路径
ENGINE_HANDLERS = {
    'agent': 'src.engine.agent_m.AgentHandler',
    'ssh': 'src.engine.ssh_m.SSHHandler',
    'salt': 'src.engine.salt_m.SaltHandler',
    # 'aliyun': 'src.engine.aliyun.AliyunHandler',
}
#  ############## SSH模式的配置 ###############
SSH_PRIVATE_KEY = '私钥的路径'
SSH_PORT = '22'  # 端口
SSH_USER = 'cmdb'  # 用户名

"""资产获取方式"""
PLUGINS_DICT = {
    "basic": 'src.plugins.basic.Basic',
    'disk': 'src.plugins.disk.Disk',
    'memory': 'src.plugins.memory.Memory',
    'nic': 'src.plugins.network.Network',
    "cpu": "src.plugins.cpu.Cpu",
    "board": "src.plugins.main_board.MainBoard",
}

# 公钥
PUB_KEY = b'LS0tLS1CRUdJTiBSU0EgUFVCTElDIEtFWS0tLS0tCk1JR0pBb0dCQUtmbWxSc2krbDdYVHo4VWo0TTZraXVrSHhRenUxR3I4T1FoOUxrMGx2OUQ5WGJueXRVcjlRVy8KRVdFOGpCZHRoTjY0WFczRDFERnlJMTRlTE1qdy9Sdm9oNVlLaTVsREZUa0I3d0l4Z251U3EvMVZmd0JuczZrQgp3anBuU3lCY00yWFJNYzE0ZUY1anhYWllUTmx0K2lLT3Q1ZE5pY3phelNQbERaV1VTMDJUQWdNQkFBRT0KLS0tLS1FTkQgUlNBIFBVQkxJQyBLRVktLS0tLQo='
# 调试模式是否开启
DEBUG = True

# 资产提报api
HOST_ASSET_API = "http://127.0.0.1:8000/api/asset"

# 主机信息存放地址
CERT_FILE_PATH = os.path.join(BASE_DIR, 'config', 'cert')
# 日志文件
LOG_FILE_PATH = os.path.join(BASE_DIR, "log", "cmdb.log")
# 客户端请求认证密钥
URL_AUTH_KEY = "ADLKFJOIER"
