def main():

    d={'one':1,'two':4,'three':5}
    print(d,type(d))

    for k in sorted(d.keys()):
        print(k,d[k],end="\n")

    d["newkey"]=50
    for k in sorted(d.keys()):
        print(k,d[k],end="\n")

main()