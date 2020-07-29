#sorting the sorted lists using one loop.
list1=[10,20,30,40,60,70,80]
list2=[5,15,25,35,45,60]
result=[]
n=len(list1)
m=len(list2)
i=0
j=0
while i<n and j<m:
    if(list1[i]<=list2[j]):
        result.append(list1[i])
        i+=1
    else:
        result.append(list2[j])
        j+=1
result=result+list1[i:]+list2[j:]
print(result)