#list to dict using list comprehension
list1=[1,2,3,4,5,7,8]
list2=["a","b","c","d","e"]

m=min(len(list1),len(list2))
res={list1[i]:list2[i] for i in range(m)}

print(res)