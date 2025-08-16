def sum_of_elements(lst):
    res=[]
    for i in lst:
        sum1=0
        while i!=0:
            rem=i%10
            sum1+=rem
            i//=10
        res.append(sum1)
    return res


lst=[]
limit=int(input("enter the number of elements to be inserted: "))
for i in range(limit):
    element=int(input("enter the element: "))
    lst.append(element)
print(sum_of_elements(lst))
