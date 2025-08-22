lst=[]
entries=int(input("enter the number of entries you need: "))
for i in range(entries):
    element=int(input("enter the element: "))
    lst.append(element)

it=iter(lst)

print(next(it))
print(next(it))
