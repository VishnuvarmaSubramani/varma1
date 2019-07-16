string1,string2=list(map(str,input().split()))
x=0
for i in range (0,len(string1)):
	if string1[i]!=string2[i]:
		x=x+1
if(x==1):
	print("yes")
else:
	print("no")
