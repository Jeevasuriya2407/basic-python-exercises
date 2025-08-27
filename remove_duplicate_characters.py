name=input("enter the name: ")
sub_str=""

for i in range(len(name)):
    if name[i] not in sub_str:
        sub_str+=name[i]
print(sub_str)
