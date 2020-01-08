#prime number or not.
a=int(input('Enter a number : '))
count=0
for i in range(1,a):
    if a%i==0:
        count=count+1
if count==1:
    print(a,' is a prime number')
else:
    print(a,' is not a prime number')