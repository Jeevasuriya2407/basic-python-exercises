def maximum(lst):
    maxi=0
    for i in lst:
        if maxi<i:
            maxi=i
    return maxi
def minimum(lst):
    mini=lst[0]
    for i in range(1,len(lst)):
        if mini>lst[i]:
            mini=lst[i]
    return mini

lst=[]
range1=int(input("number: "))
for i in range(range1):
    num=int(input("enter the value: "))
    lst.append(num)
maximum=maximum(lst)
minimum=minimum(lst)

print(maximum)
print(minimum)
