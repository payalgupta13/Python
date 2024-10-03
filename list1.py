list1 =[]
n=int(input('Enter number of elements in first list : '))
for i in range(n):
    value=int(input('enter {} value of list : '.format(i+1)))
    list1.append(value) 

list2 =[]
n=int(input('Enter number of elements in second list : '))
for i in range(n):
    value=int(input('enter {} value of list : '.format(i+1)))
    list2.append(value) 

print('list 1 : ',list1)
print('list 2 : ',list2)
tuple1=tuple(list1+list2)
print(tuple1)
