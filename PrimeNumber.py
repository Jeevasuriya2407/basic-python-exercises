lst=[]
entry=int(input("enter the number of elements you need to add: "))

for i in range(entry):
    values=int(input("enter the values: "))
    lst.append(values)
for i in lst:
    if i==1:
        print("it is not a prime number",i)
    else:
        if i>=2:
            for j in range(2,i):
                if i%j==0:
                    print("it is not a prime number",i)
                    break
            else:
                print("it is a prime number",i)
    

