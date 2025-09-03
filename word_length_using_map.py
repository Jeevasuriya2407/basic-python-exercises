lst=[]
entries=int(input("enter the number of entries: "))
for i in range(entries):
    element=input("enter the elements:  ")
    lst.append(element)
    
map_list=list(map(lambda x: len(x),lst))

print(map_list)
