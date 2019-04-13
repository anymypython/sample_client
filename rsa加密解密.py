import rsa
import base64

# ######### 1. 生成公钥私钥 #########
pub_key_obj, priv_key_obj = rsa.newkeys(1024)  # 128 字节 -11  117

pub_key_str = pub_key_obj.save_pkcs1()
pub_key_code = base64.standard_b64encode(pub_key_str)

priv_key_str = priv_key_obj.save_pkcs1()
priv_key_code = base64.standard_b64encode(priv_key_str)

print(pub_key_code)
print(priv_key_code)


# # ######### 2. 加密 #########
def encrypt(value_bytes):
    key_str = base64.standard_b64decode(pub_key_code)
    pk = rsa.PublicKey.load_pkcs1(key_str)

    msg_list = []
    for i in range(0, len(value_bytes), 117):
        chunk = value_bytes[i:i + 117]
        val = rsa.encrypt(chunk, pk)
        msg_list.append(val)
    return b''.join(msg_list)


str = 'alex' * 1000
ret = encrypt(str.encode('utf-8'))
# print(ret)
# print(len(ret))


#
# # ######### 3. 解密 #########
def decrypt(value_bytes):
    key_str = base64.standard_b64decode(priv_key_code)
    pk = rsa.PrivateKey.load_pkcs1(key_str)

    msg_list = []
    for i in range(0, len(value_bytes), 128):
        chunk = value_bytes[i:i + 128]
        val = rsa.decrypt(chunk, pk)
        msg_list.append(val)
    return b''.join(msg_list)


# ret = decrypt(ret)
# print(ret)
# print(len(ret))
