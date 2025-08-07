num1=int(input("number: "))
num2=int(input("number: "))

series=int(input("enter the number of iterations you need: "))
print(num1,end="")
print(num2,end="")

for i in range(series):
    result=num1+num2
    print(result,end="")
    num1=num2
    num2=result
