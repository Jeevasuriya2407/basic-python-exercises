def fact(n):
    if n==1:
        return 1
    else:
        return n*fact(n-1)


num1=int(input("number: "))
print(fact(num1))
