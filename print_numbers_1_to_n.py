def print_numbers(num):
    if num==0:
        return
    else:
        print_numbers(num-1)
        print(num,end=" ")


num1=int(input("number: "))
print_numbers(num1)

