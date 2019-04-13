from config import settings
from lib.moduler_string import import_string


# from src.engine.agent import AgentHandler
# from src.engine.salt import SaltHandler
# from src.engine.ssh import SSHHandler

def run():
    """资产采集的入口"""
    engine_path = settings.ENGINE_HANDLERS.get(settings.ENGINE)

    engine_class = import_string(engine_path)
    obj = engine_class()
    obj.handler()
