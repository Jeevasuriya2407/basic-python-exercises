def pair_sum(lst,target):
    left=0
    right=len(lst)-1
    
    for i in range(len(lst)):
        s=lst[left]+lst[right]
        if s==target:
            return [lst[left],lst[right]]
        elif s<target:
            left+=1
        else:
            right-=1
    return []
            
        

lst=[]
entries=int(input("number: "))
for i in range(entries):
    element=int(input("add the element: "))
    lst.append(element)
target=int(input("enter the target: "))
res=pair_sum(lst,target)
print(res)
