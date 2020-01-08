a=int(input('ENter co-efficent a : '))
b=int(input('ENter co-efficent b : '))
c=int(input('ENter co-efficent c : '))
d=(b**2)-(4*a*c)
print(d)
if d<0:
    print('No real roots for equation.')
elif d==0:
    x = -(b/(2*a))
    print('root is one and it is ',x)
else:
    x = (((-b)+(d**0.5))/(2*a))
    y = (((-b)-(d**0.5))/(2*a))
    print('two roots for equation and first is ',x,' and second is ',y)
