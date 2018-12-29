class c1:
    def __init__(self):
        print("object constructed")
    def fun1(self):
        print("hi hello")
    def fun2(self):
        print("how are you")

class c2:
    def __init__(self,value=99):
        self._v=value
        print("object constructed",self._v)
    def fun1(self):
        print("hi hello",self._v)
    def fun2(self):
        print("how are you",self._v)

def main():
    obj1=c1()
    obj1.fun1()
    obj1.fun2()
    obj2=c2()
    obj2.fun1()
    obj2.fun2()

main()