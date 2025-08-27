lst=[]
no_of_elements=int(input("enter the number: "))

for i in range(no_of_elements):
    elements=int(input("enter the element: "))
    lst.append(elements)

for i in range(len(lst)):
    for j in range(i+1,len(lst)):
        if lst[i]>lst[j]:
            temp=lst[i]
            lst[i]=lst[j]
            lst[j]=temp
tup=tuple(lst)
k=int(input("enter the k element value: "))
print(f"the largest two elements is {tup[-k:]} ")
print(f"the smallest two elements is {tup[:k]}")            
