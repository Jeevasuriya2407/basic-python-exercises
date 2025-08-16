def count(n):
    count=0
    while n!=0:
        rem=n%10
        count+=1
        n//=10
    return count

num1=int(input("number: "))
print(count(num1))
