def sort(arr):
    le=len(arr)
    for i in range(le):
        for j in range(le-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
arr = [2,1,4,21,12,41,15]
sort(arr)
for i in range(len(arr)):
    print(arr[i],end=' ')