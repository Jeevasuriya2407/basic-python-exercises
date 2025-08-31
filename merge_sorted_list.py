def merge_sorted_list(lst,lst1):
    i=0
    j=0
    res=[]
    while i<len(lst) and j<len(lst1):
        if lst[i]<lst1[j]:
            res.append(lst[i])
            i+=1
        else:
            res.append(lst1[j])
            j+=1
    res.extend(lst[i:])
    res.extend(lst1[j:])
    return res


lst=[]
entries=int(input("enter the number of elements to be inserted: "))

for i in range(entries):
    element=int(input("enter the element: "))
    lst.append(element)
lst1=[12,4,8,1,3]

for i in range(len(lst)):
    for j in range(i+1,len(lst)):
        if lst[i]>lst[j]:
            temp=lst[i]
            lst[i]=lst[j]
            lst[j]=temp

for i in range(len(lst1)):
    for j in range(i+1,len(lst1)):
        if lst1[i]>lst1[j]:
            temp=lst1[i]
            lst1[i]=lst1[j]
            lst1[j]=temp

res=merge_sorted_list(lst,lst1)
print(res)
