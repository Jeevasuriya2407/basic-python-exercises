lst=[]
entries=int(input("enter the number of entries you need: "))
for i in range(entries):
    elements=input("enter the element you need: ")
    lst.append(elements)
first_word=list(filter(lambda x:x.startswith('b'),lst))
print(first_word)
