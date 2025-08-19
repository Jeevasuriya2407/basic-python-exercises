def perfect(num,factors=1):
    if num==factors:
        return 0
    if num%factors==0:
        return factors+perfect(num,factors+1)
    else:
        return perfect(num,factors+1)
   
        
def is_check(num):
    if num==perfect(num):
        return True
    else:
        return False


num=int(input("enter the number: "))

if is_check(num):
    print("perfect number")
else:
    print("not perfect number")
