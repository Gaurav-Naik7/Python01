def Marvellous(value):
    if value%5==0:
        print("True")
    else:
        print("False")

def main():
    no=int(input("Enter a number: "))
    Marvellous(no)

if __name__=="__main__":
    main()
