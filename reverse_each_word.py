text=input("enter the text: ")
words=text.split()
reverse=[]

for i in words:
    rev=i[::-1]
    reverse.append(rev)

result=' '.join(reverse)
print(result)
