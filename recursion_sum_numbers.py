def Natural_Number(n):
    if n==1:
        return 1
    else:
        return n+Natural_Number(n-1)


num1=int(input("number: "))
print(Natural_Number(num1))
