lst=[]
entries=int(input("enter the number of entries you need: "))
for i in range(entries):
    elements=int(input("enter the element you need: "))
    lst.append(elements)
filter_evens=list(filter(lambda x:x%2==0,lst))
print(filter_evens)
