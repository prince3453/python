str1="this is an animal"
str2=input("Enter the substring : ")
n=int(input("ENter the position where you want to enter substring : "))
result=str1[:n] + str2 + str1[n:]
print(result)