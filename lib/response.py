class BaseResponse():
    """
    基本响应格式
    """

    def __init__(self):
        self.status = True
        self.error = None
        self.data = None

    @property
    def dict(self):
        return self.__dict__
