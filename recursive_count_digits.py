def count_digits(num,count=0):
    if num==0:
        return count
    else:
        return count_digits(num//10,count+1)
   

num=int(input("number: "))
print(count_digits(num))
