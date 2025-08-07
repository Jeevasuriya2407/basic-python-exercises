num1=int(input("number: "))
temp=num1

result=0

while temp!=0:
    rem=temp%10
    fact=1
    for i in range(1,rem+1):
        fact=fact*i
    result+=fact
    temp//=10

if(result==num1):
    print("it is a strong number",result)
else:
    print("it is not a strong number",result)
