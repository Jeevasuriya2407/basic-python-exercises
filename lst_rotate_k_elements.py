def lst_rotate(lst,k):
    k=k%len(lst)
    
    return lst[-k:]+lst[:-k]

lst=[]
entries=int(input("enter the number of elements to be inserted: "))

for i in range(entries):
    element=int(input("enter the element: "))
    lst.append(element)

k=int(input("enter the number of k rotations: "))
res=lst_rotate(lst,k)
print(res)
