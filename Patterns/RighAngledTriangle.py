"""
Enter N: 5
* 
* * 
* * * 
* * * * 
* * * * * 
"""




# n=int(input("Enter N: "))

# out="*"
# for i in range (1,n+1):
#   for j in range(i):

#     print("*", end="")

#   print()
    

n=int(input("Enter N: "))

for i in range(n):
  for j in range(i+1):
    print("*",end=" ")
  print()



    
