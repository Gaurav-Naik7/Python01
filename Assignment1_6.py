def Marvellous(value):
    if value>0:
        print("Positive Number")
    elif value<0:
        print("Negative Number")
    else:
        print("Zero")

def main():
    no=int(input("Enter a number: "))
    Marvellous(no)

if __name__=="__main__":
    main()
