def is_power(num,power):
    if num==0:
        return 0
    else:
        rem=num%10
        return rem**power+is_power(num//10,power)
def is_Armstrong(num):
    digits=len(str(num))
    return num==is_power(num,digits)
    


num=int(input("number: "))
if is_Armstrong(num):
    print("armstrong number")
else:
    print("it is not a armstrong number")
