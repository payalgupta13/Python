tup1=(('333','33'),('1416','55'))
a,b=tup1
newlista=[]
newlistb=[]
arr=[]
for i in a:
    newlista.append(int(i))
arr.append(newlista)
for i in b:
    newlistb.append(int(i))
arr.append(newlistb)
finaltup=tuple(map(tuple, arr))
print(finaltup)
