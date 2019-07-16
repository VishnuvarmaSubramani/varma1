string1,string2=map(str,input().split())
for i in string1:
    x=string1.count(i)
for j in string2:
    y=string2.count(j)
if(x==y):
    print("yes")
else:
    print("no")
