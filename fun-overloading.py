def main():
    fun0(1,2,3)
    fun2()
    fun2(8,9,10)
    fun2(11,12)
    fun3(8)
    fun3(5,None,2)
    fun4(4,5,6,7,8,9,0,2,3,5,3,7,5,8,3)
    fun5(one='kishan',duck='arjun',two=652143)
    fun6(1,2,3,4,5,6,7,8,9,pm="Mr.N Modi",cm="vijay rupani")

    for i in fun7():
        print(i,end=" ")

    a,b,c=fun8(1,2)
    print(" ",end="\n\n")
    print(a,b,c)

def fun0(x,y,z):
    print(x,y,z)

def fun2(x=3,y=4,z=5):
    print(x,y,z)

def fun3(x=3,y=None,z=5):
    if y is None:
        y=99
    print(x,y,z)

def fun4(x=3,y=4,z=5,*args):
    print(x,y,z)
    for n in args:
        print(n,end=" ")

def fun5(**kwargs):
    print("named arguments are ",kwargs['one'],kwargs['duck'],kwargs['two'])

def fun6(a,b,c,*args,**kwargs):
    print(a,b,c)
    for n in args:
        print(n,end=" ")
    for i in kwargs:
        print(i,"=",kwargs[i])

def fun7():
    return range(25)

def fun8(x,y):
    p=x+y
    q=x-y
    r=x*y
    return(p,q,r)

main()