l=list(map(int, input("Enter list").split(",")))

n=int(input("Enter the number"))

count=0
i=0
for item in l:
  if item == n:
   count=count+1

print(count)
