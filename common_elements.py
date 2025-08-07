lst=[]
n=(int(input("enter the number of elements the list should contain: ")))
for i in range(n):
    element=int(input("enter the element to be added: "))
    lst.append(element)
lst1=[1,2,3,4]

lst2=[]

for i in lst:
   for j in lst1:
       
       if i==j:
           lst2.append(i)
print("the elements in list1 ",lst)
print("the elements in list2 ",lst1)
print("the elements in list3 ",lst2)
