def sum_of_naturalnumbers(num):
    if num == 1:   # base case
        return 1
    else:
        return num + sum_of_naturalnumbers(num - 1)  # recursive case

n = int(input("Enter a number: "))
res = sum_of_naturalnumbers(n)
print("Sum of first", n, "natural numbers is:", res)
