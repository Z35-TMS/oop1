class TestClass:
    a = 0

    def __init__(self, a):
        self.a = a

    def __eq__(self, other):
        return self.a == other.a

    def get(self):
        return self.a

    def __hash__(self):
        return 7

    def __call__(self, val):
        return self.a * val

    def __str__(self):
        return "TestClass()"

    def __repr__(self):
        return "TestClass"

    def __add__(self, other):
        return self.a + other.a

    @classmethod
    def set(cls):
        cls.a = 10

