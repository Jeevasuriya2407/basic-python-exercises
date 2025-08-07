num=int(input("enter the number: "))
rev=0
temp=num

while temp!=0:
    rem=temp%10
    rev+=rem**3
    temp//=10

if num==rev:
    print("it is an armstrong number",rev)
else:
    print("it is not an armstrong number",rev)
