
# Calculator application


num1=int(input("Enter Num1:"))
num2=int(input("Enter Num2:"))

operation=input("Enter an operation you want to perform(+,-,*,/): ")

if operation == "+":
  Total=num1+num2
  print(f"Sum is {Total}")

elif operation == "-":
  Difference=num1-num2
  print(f"Difference is {Difference}")

elif operation == "*":
  Product=num1*num2
  print(f"Product is {Product}")

elif operation == "/":
  Quotient=num1/num2
  print(f"Quotient is {Quotient}")

else:
  print("Enter a valid operator")

    
    
  