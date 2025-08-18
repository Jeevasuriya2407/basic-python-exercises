def sum_of_digits(num):
    if num==0:
        return 0
    else:
        return (num%10)+sum_of_digits(num//10)

n=int(input("number: "))
res=sum_of_digits(n)
print(res)
