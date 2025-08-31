def mov_zero_right(lst):
    left=0
    for right in range(len(lst)):
        if lst[right]!=0:
            lst[left],lst[right]=lst[right],lst[left]
            left+=1
    return lst

            
lst=[]
entries=int(input("number: "))
for i in range(entries):
    element=int(input("add the element: "))
    lst.append(element)

res=mov_zero_right(lst)
print(res)
