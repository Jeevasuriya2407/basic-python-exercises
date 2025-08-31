words=input("enter the string value: ")
lst=words.split()
dict1={}

for i in lst:
    dict1[i]=dict1.get(i,0)+1
print(dict1)
    
