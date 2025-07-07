"""a= input()

x,y,z=a.split(",")

num1=int(x)
num2=int(y)
num3=int(z)


if(num2>num1 and num2>num3):
  print(num2)

elif(num1>num2 and num1>num3):
  print(num1)

else:
  print(num3)"""




a=input("Enter 3 values seperated by',' : ")


x,y,z=a.split(",")

num1=int(x)
num2=int(y)
num3=int(z)

great=0


if(num1>num2):
  if(num1>num3):
    great=num1
  else:
    great=num3


elif(num2>num1):
  if(num2>num3):
    great=num2
  else:
    great=num3


elif(num3>num1):
  if(num3>num2):
    great=num3
  else:
    great=num2


print(great)

  
