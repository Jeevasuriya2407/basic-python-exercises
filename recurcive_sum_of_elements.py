def sum_of_elements(lst):
    if not lst:
        return 0
    return lst[0]+sum_of_elements(lst[1:])

lst=[]
entries=int(input("number of entries: "))
for i in range(entries):
    element=int(input("enter the value: "))
    lst.append(element)
res=sum_of_elements(lst)
print(res)
