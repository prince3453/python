a = int(input('Enter a number : '))
x=0
y=0
z=1
print(x,'',y,'',z,end=" ")
for i in range(a-1):
    x=y
    y=z
    z=x+y
    if z>a:
        break
    else:
        print(z,end=" ")