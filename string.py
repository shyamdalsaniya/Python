def main():
    s = r"this is an \n exmple of string"
    print(s)

    s1 = "hi hello " "how are you"
    print(s1)

    x = 30
    s2 = "this is x={} string".format(x)
    print(s2)

    y = 15
    s3 = "this is %d %d string" % (x, y)
    print(s3)

    s4 = "this {0} {1} {0} {0} {1} string".format("hello", "hi")
    print(s4)

    print('{0: ^11}'.format("hello"))
    print('{0:#^11}'.format("hello"))
    print('{0:@^11}'.format("hello"))
    print('{0:(^11}'.format("hello"))
    print('{0:^^11}'.format("hello"))

    x = x + 5
    print(x, type(x))
    x = str(x)
    x = x + "5"
    print(x, type(x))

    # fibonaci series
    a, b = 1, 1
    while a < 100 or b < 100:
        print(a, " ", b, " ", end=" ")
        a = a + b
        b = a + b


main()