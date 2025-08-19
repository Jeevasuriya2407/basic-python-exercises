def maximum(lst):
    if len(lst)==1:
        return lst[0]
    else:
        return max(lst[0],maximum(lst[1:]))

lst=[]
entries=int(input("number of entries: "))
for i in range(entries):
    element=int(input("enter the value: "))
    lst.append(element)
res=maximum(lst)
print(res)
