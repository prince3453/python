def fact(a):
    i=1
    while a>=1:
        i=i*a
        a=a-1
    print(i)
a=int(input('Enter factorial number : '))
fact(a)