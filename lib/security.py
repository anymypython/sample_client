"""
数据加密
"""
import base64
import rsa
from config import settings


def encrypt(value_bytes):
    """
    加密
    :param value_bytes:  加密的数据, bytes类型 
    :return:   加密后的数据
    """
    key_str = base64.standard_b64decode(settings.PUB_KEY)  # 节码成字符串
    pk = rsa.PublicKey.load_pkcs1(key_str)  # 加载公钥

    msg_list = []
    # 加密数据限定了1024字节, 可以设置更高
    for i in range(0, len(value_bytes), 117):
        chunk = value_bytes[i:i + 117]  # 切片数据
        val = rsa.encrypt(chunk, pk)  # 加密数据
        msg_list.append(val)  # 追加到列表中
    return b"".join(msg_list)
