num1=int(input("enter the number: "))
temp=num1
sum1=0

for i in range(1,num1):
    if temp%i==0:
        sum1+=i
if sum1==num1:
    print("it is a perfect number",sum1)
else:
    print("it is not a perfect number",sum1)
