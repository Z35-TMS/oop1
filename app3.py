class TestClass():

    a = 4

    def __init__(self):
        self.b = 5

    @classmethod
    def get(cls):
        return cls.a

    @staticmethod
    def sum(a, b):
        return a + b

    def get_b(self):
        return self.b

    @property
    def method(self):
        return self.b

    @method.setter
    def method(self, value):
        self.b = value

    @method.deleter
    def method(self):
        self.b = 0


if __name__ == "__main__":
    obj = TestClass()
    print(obj.get())
    print(TestClass.get())
    print(obj.get_b())
    # print(TestClass.get_b())
    print(obj.sum(3, 6))
    print(TestClass.sum(3, 6))

    obj.arg = 'KDKDKD'
    print(obj.arg)

    print(obj.method)
    obj.method = 6
    print(obj.method)
    del obj.method
    print(obj.b)


    obj.get_b = "TExt"
    print(obj.get_b)
    del obj.__dict__["get_b"]
    print(obj.get_b())