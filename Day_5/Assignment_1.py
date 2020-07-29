#To sort in increasing order with zeros at end. 
def fun(x):
    return x==0
a=[0,1,2,10,4,1,0,56,2,0,1,3,0,56,0,4]
a.sort()
a.sort(key=fun)
print(a)
