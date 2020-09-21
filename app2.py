class A:
    def __init__(self, a):
        self.a = a

    def get(self):
        print(self.__class__)
        print("A")
        return self.a


class B:
    a = "Class B"

    def __init__(self):
        print("init B")

    def get(self):
        print(self.__class__)
        print("B")
        return self.a

    def set(self, value):
        print("get() B")
        self.a = value


class C(A, B):

    def get(self):
        res = super().get()
        return str(res) * 4


if __name__ == "__main__":
    c = C(3)
    print(c.a)
    print(c.__dict__)
    print(c.get())