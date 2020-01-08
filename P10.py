def large(n1,n2,n3):
    
    if(n1>n2 and n2>n3):
        print(n1," is largest.")
    elif(n2>n3):
        print(n2," is largest.")
    else:
        print(n3," is largest.")
n1=int (input("Enter first number: "))
n2=int (input("Enter second number: "))
n3=int (input("Enter third number: "))
large(n1,n2,n3)