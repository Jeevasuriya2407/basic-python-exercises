print("String methods: ")

name=input("enter you name: ")
name1=input("name: ")
username=input("enter the username: ")
sentence=input("sentence: ")

s=name.replace("j","g")
print(name.capitalize())
print(name1.upper())
print(name1.lower())
print(sentence.count("is"))
l=sentence.find("good")

print(s)
print(l)

if username.isalpha():
    print("valid username")
else:
    print("only characters can be allowed")

if username.isalnum():
    print("valid username")
else:
    print("it can accept only numbers and digits")


