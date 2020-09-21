class A():
    pass

class B():
    __slots__ = ("var",)

    a = 5
    
    def get(self):
        return "kdkdk"


if __name__ == "__main__":
    a = A()
    b = B()
    print(dir(a))
    print()
    print(dir(b))

    a.var = 7
    print(a.var)
    print(a.__dict__)

    # print(b.__dict__)
    b.var = 4
    print(b.var)
    b.var = lambda x: str(x) * 4
    print(b.var(465))

    print(b.get())
    # b.get = "value"
    # print(b.get)

    print(b.a)