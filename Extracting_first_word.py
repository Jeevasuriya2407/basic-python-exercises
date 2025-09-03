lst=[]
n=int(input("number of characters you need to be included: "))
for i in range(n):
    words=input("enter the word: ")
    lst.append(words)
first_word=list(map(lambda w:w[0],lst))
print(first_word)
