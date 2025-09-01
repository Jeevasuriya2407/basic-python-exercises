def my_countdown(num):
    for i in range(num,-1,-1):
        yield i


n=int(input("number: "))
countdown=my_countdown(n)

for i in countdown:
    print(i)
