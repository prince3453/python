l1 = ['1','2','3','4','5','6','7']
l2 = ['a','b','c','d','f','e','g']
def dict(l1,dict2):
    for i in range(len(l1)):
       dict2[i]=l1[i]
    return dict2
dict2={}
print(dict(l1,dict2))
print(dict(l2,dict2))

