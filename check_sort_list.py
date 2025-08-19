def sort_list(lst):
    if len(lst)<=1:
        return True
    else:
        return lst[0]<=lst[1] and sort_list(lst[1:])
lst=[]
length=int(input("enter the length of a list: "))
for i in range(length):
    element=int(input("entrer the number: "))
    lst.append(element)
if sort_list(lst):
    print("sorted")
else:
    print("not sorted")
