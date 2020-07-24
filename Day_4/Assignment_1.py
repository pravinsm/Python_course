str1=input("Enter the String : ")#"what we think we become; we are Python programmer"
str2=input("Enter the substring : ")#"we"
index=0
while(1):
    index=str1.find(str2,index)
    if(index == -1):
        break
    print(index)
    index=index+len(str2)
