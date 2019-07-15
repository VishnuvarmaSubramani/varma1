x=int(input())
d=0
rev=0
while x>0 :
 d=x%10
 rev=(rev*10+d)
 x=(x//10)
print(rev) 
