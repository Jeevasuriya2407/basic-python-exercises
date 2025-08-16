def sum_of_number(num):
    sum1=0
    while num!=0:
        rem=num%10
        sum1+=rem
        num//=10
    return sum1
n=int(input("enter the number: "))
print(sum_of_number(n))
