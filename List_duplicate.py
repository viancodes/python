l=list(map(int,input().split(",")))


l2=[]

for i in l:
  if i in l2:
    continue
  else:
    l2.append(i)

print(l2)