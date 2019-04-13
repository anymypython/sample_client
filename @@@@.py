# # from functools import wraps
# #
# # tt = True
# #
# #
# # def par(boo=tt):
# #     def outer(func):
# #         @wraps(func)
# #         def inner(*args, **kwargs):
# #             if boo:
# #                 print(*args, **kwargs)
# #             ret = func(*args, **kwargs)
# #             print(*args, **kwargs)
# #             return ret
# #
# #         return inner
# #
# #     return outer
# #
# #
# # @par()
# # def p(x):
# #     print("yiyayiyao", x)
# #
# #
# # p("aaaa")
#
# def wrapper(func):
#     def inner():
#         func()
#
#     return inner
#
#
# def f():
#     print("f1ddd")
#
#
# f = wrapper(f)
# import time
# time.sleep(1)
# f()


di1 = {1: "22", 2: "33"}
di2 = {1: "22", 3: "33"}

print(set(di1) & set(di2))

