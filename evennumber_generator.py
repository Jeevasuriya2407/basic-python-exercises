def even_numbers(n):
    for i in range(2,n+1,2):
        yield i

n=int(input("enter the range of numbers to be fetched: "))
for num in even_numbers(n):
    print(num)
