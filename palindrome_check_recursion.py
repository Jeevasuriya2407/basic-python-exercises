def isPalindrome(name):
    if len(name)<1:
        return True
    if name[0]==name[-1]:
        
        return isPalindrome(name[1:-1])
    else:
        return False

name=input("enter the name: ")
if isPalindrome(name):
    print(name,"it is a palindrome")
else:
    print(name,"it is not a palindrome")
