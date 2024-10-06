list_A=[4,4,8,4,9,7,9,9,9,7]
list1=[]
list2=[]

for x in list_A:
           if (x not in list1):
                   list1.append(x)
                   i=0
                   for j in list_A :
                        if(x==j):
                              i=i+1
                   list2.append(i)
print(list1)
print(list2)