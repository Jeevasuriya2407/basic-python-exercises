def N_Number(n):
    if n==0:
        return
    else:
        N_Number(n-1)
        print(n,end=" ")


num1=int(input("number: "))
N_Number(num1)
