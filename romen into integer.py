romen=['I','II','III','IV','V','VI','VII','VIII','IX','X','XI','XII','XIII','XIV','XV','XVI','XVII','XVIII','XIX','XX']
integer=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
romen_letter=str(input())
for i in range(20):
  if(romen_letter==romen[i]):
    print(integer[i])
    break
