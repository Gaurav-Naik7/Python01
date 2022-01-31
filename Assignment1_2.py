def ChkNum(value):
    if value%2==0:
        return "Even number"
    else:
        return "Odd number"

def main():
    no=int(input("Enter a number: "))
    ret=ChkNum(no)
    print(ret)

if __name__=="__main__":
    main()
