import hashlib
from config import settings


def gen_key(ctime):
    # ctime 请求时间
    # 动态生成密钥, 身份验证
    key_str = f"{settings.URL_AUTH_KEY}|{ctime}"
    md5 = hashlib.md5()  # 可以加盐
    md5.update(key_str.encode("utf-8"))
    return md5.hexdigest()
