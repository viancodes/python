"""
Enter N: 5
* * * * * 
* * * * * 
* * * * * 
* * * * * 
* * * * * 

"""


n=int(input("Enter N: "))


for i in range(n):   #used for no.of rows
  for j in range(n):   #used for no.of columns
    print("*",end=" ")  #end="" is used to avoid printing in new line
  print()