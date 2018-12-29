def main():
    print(2+3)
    print(2*3)
    print(12/3)
    print(21%4)

    x,y=divmod(21,4)
    print(x,y)

    a=3
    a+=3
    print(a)
    a-=3
    print(a)
    a*=3
    print(a)
    a/=3
    print(a)

    a=5/3
    print(a)
    a=5//3
    print(a)

    #boolean
    print(5>3)
    print(5<3)

    print(7>=7)
    print(7<=5)

    print(5==5)
    print(5!=5)



    x,y=5,6
    print(id(x)," ",id(y))
    print(x is not y)
    y=5
    print(id(x)," ",id(y))
    print(x is not y)


    l1=[1,2,3,4,5,6,7,8]
    print(l1[0],"\n\n")
    print(l1[0:5],"\n\n")

    l1[:]=range(25,45)
    print(l1,end="\n\n")

    print(l1[0:20:3],end="\n\n")

    l1[0:6:2]=(88,99,77)
    print(l1)

main()