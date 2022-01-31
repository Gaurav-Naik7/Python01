def Add(value1,value2):
    addition=value1+value2
    return addition

def main():
    no1=int(input("Enter first number: "))
    no2=int(input("Enter second number: "))
    ret=Add(no1,no2)
    print("Addition of the two numbers is ",ret)

if __name__=="__main__":
    main()
