def fibonacci(n):
    a,b=0,1
    while a<n:
        yield a
        a,b=b,a+b
            


num=int(input("enter the range: "))
for i in fibonacci(num):
    print(i)
