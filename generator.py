def main():
    for i in inclusive_range(0,25,3):
        print(i,end=" ")
    print(end="\n\n")
    for i in inclusive_range1(25):
        print(i,end=" ")
    print(end="\n\n")
    for i in inclusive_range1(5,25):
        print(i,end=" ")
    print(end="\n\n")
    for i in inclusive_range1(5,25,2):
        print(i,end=" ")

#yield is return value at between execution of program at calling function
def inclusive_range(start,stop,step):
    i=start
    while i <= stop:
        yield i
        i+=step

def inclusive_range1(*args):
    num=len(args)
    if num < 1:
        raise TypeError("atleast on argument is required")
    elif num == 1:
        start=0;
        stop=args[0];
        step=1
    elif num == 2:
        start,stop=args
        step=1
    elif num == 3:
        start,stop,step=args
    else: raise TypeError("argument can't exceed 3.you gave {} ".format(num))

    i=start
    while i <= start:
        yield i
        i+=step

main()