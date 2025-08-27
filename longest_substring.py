name=input("enter the name: ")
sub_str=""
sub_str1=""

for i in range(len(name)):
    for j in range(i,len(name)):
        
        if name[j] not in sub_str:
            sub_str+=name[j]
        else:
            break
    if len(sub_str1)<len(sub_str):
        sub_str1=sub_str
    sub_str=""
print(sub_str1)
