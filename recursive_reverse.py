def reverse(lst):
    if not lst:
        return []
    return [lst[-1]]+ reverse(lst[:-1])

lst=[]
entries=int(input("number of entries: "))
for i in range(entries):
    element=int(input("enter the value: "))
    lst.append(element)
res=reverse(lst)
print(res)
