x=int (input("Enter number x : "))
y=int (input("Enter number y : "))
if x>y:
    x,y=y,x
while x<=y:
    if x%2==0:
        print(x,end=' ')
    x=x+1
    