n1,n2=input().split()
n1=int(n1)
n2=int(n2)
lis=[]
if(n1>1 and n2>1):
    for i in range (n1,n2+1):
        for j in range (2,i):
            if (i%j==0):
                break
        else:
            lis.append(i)
print(len(lis))
