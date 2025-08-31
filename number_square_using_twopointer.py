def squares(lst):
    result=[]
    left=0
    right=len(lst)-1
    
    for i in range(len(lst)):
        if abs(lst[left])<abs(lst[right]):
            result.append(lst[left]**2)
            left+=1
        else:
            result.append(lst[right]**2)
            right-=1
    return result

lst=[]
entries=int(input("number: "))
for i in range(entries):
    element=int(input("add the element: "))
    lst.append(element)
    
res=squares(lst)
print(res)
