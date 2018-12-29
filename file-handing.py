def main():

    try:
        fh=open("asd.txt")
    except IOError as e:
        print("simple exception file handling",e)
    else:
        for line in fh:
            print(line.strip())

main()