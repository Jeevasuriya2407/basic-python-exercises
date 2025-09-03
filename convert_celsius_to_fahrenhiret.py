lst=[]
entries=int(input("enter the number of entries: "))
for i in range(entries):
    element=int(input("enter the elements:  "))
    lst.append(element)
    
map_list=list(map(lambda x:(x*9/5)+32,lst))

print(map_list)
