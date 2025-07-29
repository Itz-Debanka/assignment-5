#Task 2
list=[]
for i in range(1,11):
    list.append(i)
print('original list:',list)
a=(list[0:5])
print('extracted first five elements:  ',a)

a.reverse()
print('reversed extracted elements:  ',a)