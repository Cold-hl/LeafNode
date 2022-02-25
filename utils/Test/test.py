Z = []

def xxx(xx):
    global Z
    Z.append(xx.c)

class test(object):
    def __new__(cls, *args, **kwargs):
        cls.c = args
        xxx(cls)
        return object

xy = test(1)
zz = test(2)
print(Z)