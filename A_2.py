l=[]
for i in range(0,10):
    n=i+1
    l.append(n)
print(l)
a=l[0:5]
print ("Extracted first five elements:",a )
a.reverse()
c=a[0:5]
print ("Reversed extracted elements:",c)