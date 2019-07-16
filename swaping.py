u=list(input())
v=len(u)
new=''
for i in range (0,v,2):
    u[i],u[i+1]=u[i+1],u[i]
print(*u,sep='')
