def is_duplicate(lst):
    for i in range(len(lst)):
        for j in range(i+1,len(lst)):
            if lst[i]==lst[j]:
                return True
    return False

lst=[]
length=int(input("number of elements to be entered in the list: "))
for i in range(length):
    elements=int(input("enter the number: "))
    lst.append(elements)

if is_duplicate(lst):
    print("duplicates are present")
else:
    print("duplicates are not present")

