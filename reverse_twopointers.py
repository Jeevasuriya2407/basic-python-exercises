def reverse(str1):
    str1=list(str1)
    left=0
    right=len(str1)-1
    
    str1[left],str1[right]=str1[right],str1[left]
    left+=1
    right-=1
    return ''.join(str1)

str1=input("enter the string value: ")
res=reverse(str1)
print(res)
