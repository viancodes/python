temp=float(input("Enter temperature:"))
unit=input("Enter Units(K or F or C):")

t=unit.upper()

K=0
F=0
C=0


if(t=='K'):
  F=(temp-273.15)*9/5+32
  C=(temp-273.15)
  print(f"Temperature in Fahrenheit:{F}"'\n'f"Temperature in Celcius:{C}")


elif(t=='F'):
  K=(temp-32)*5/9+273.15
  C=(temp-32)*(5/9)
  print(f"Temperature in Kelvin:{K}"'\n'f"Temperature in Celcius:{C}")

elif(t=='C'):
  K=(temp+273.15)
  F=(temp*9/5)+32
  print(f"Temperature in Kelvin:{K}"'\n'f"Temperature in Fahrenheit:{F}")

else:
  print("Choose correct option!")