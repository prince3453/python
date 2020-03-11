def binary_search(li,item):
    first = 0
    last = len(li)-1
    while(first<=last):
        mid = (first + last)//2
        if li[mid] == item :
            return mid
        elif item < li[mid]:
            last = mid - 1
        elif item > li[mid]:
            first = mid + 1
    return -1

li=[1,2,3,4,5,6,7,8]
item=int(input("Enter element you want to find : "))
result=binary_search(li,item)
if result == -1:
    print(item,"is not in the list")
else:
    print(item,"is at",result,"position")