import lib
from lib import classes

print(dir(lib))
print(dir(classes))
print(lib.__doc__)
print(lib.__name__)
print(lib.__file__)
print(dir(lib.__loader__))
try:
    print(lib.__loader__.get_code("classes"))
except ImportError as error:
    print(dir(error))
else:
    print("Без ошибок")
finally:
    print("Выполнюсь всегда")


print(dir(classes.TestClass))

obj1 = classes.TestClass(1)
obj2 = classes.TestClass(2)
print(dir(obj1))

print(id(obj1))
print(id(obj2))

print(obj1 == obj2)
print(obj1 is obj2)

obj2 = obj1
print(obj1 is obj2)
obj1.a = 3
print(obj1 == obj2)
print(obj2.a)


obj2.b = 7
print(obj2.b)
print(obj1.b)

print(obj2.get())

print(obj1.__dict__)

obj2.get = 4
print(obj2.get)

print(obj1.__dict__)
del obj2.__dict__["get"]
print(obj2.get())


val = {}
key = "key"
val[key] = "f;asldkfhh"
print(val)
val[("obj2",)] = 7
print(val)

val[obj2] = 1234
print(val)

print(obj2(8))

print(repr(obj1))
print(obj1)


ret = str("{!r}".format(obj2))
print(ret)


obj3 = classes.TestClass(17)
result = obj3 + obj2
print(result)

print(classes.TestClass.a)
print(classes.TestClass.set())
print(classes.TestClass.a)
print(obj1.a)
print(obj2.a)
print(obj3.a)