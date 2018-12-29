def main():
    print("hello world form python")
    a=60+60
    print(a)

    #this is way to write a comment

    a,b=10,15
    print(a,b)

    a,b=b,a
    print(a,b)

    print("%d %d %s"%(a,b,5*"hello"))

    #this tuple.it is static array. it can not change after it is created
    arr1=(1,2,3,5)
    print(arr1,type(arr1))

    #this is list.it is dynamic array.it can change after it is created
    arr2=[1,2,3,4,5,6]
    print(arr2,type(arr2))

    arr2.append(7)
    print(arr2)

    arr2.insert(0,90)
    print(arr2)

main()
