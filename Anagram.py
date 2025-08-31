def isAnagram(str1,str2):
    str1=str1.replace(" ","").lower()
    str2=str2.replace(" ","").lower()
    
    if len(str1)!=len(str2):
        return False
    sorted_str1=sorted(str1)
    sorted_str2=sorted(str2)
    
    return sorted_str1==sorted_str2

str1=input("enter the string1: ")
str2=input("enter the string2: ")

if isAnagram(str1,str2):
    print("it is anagram")
else:
    print("it is not an anagram")
