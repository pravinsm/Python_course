#inner lists & tuples to outer list
list1=[(1,2,3),[1,2],['a','hit','less']]
for i in range(len(list1)):
    list1.extend(list1[0])
    del list1[0]
print(list1)