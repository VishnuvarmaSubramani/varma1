x=int(input())
lis=list(map(int,input().split()))
lis1=[]
for i in lis:
  if lis.count(i)>1:
    if str(i) not in lis1:
      lis1.append(str(i))
if len (lis1)==0:
  print("unique")
else:
  lis.sort()
  print(" ".join(lis1))
