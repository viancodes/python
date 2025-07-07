m=int(input("Marks in Math: "))
s=int(input("Marks in Science: "))
e=int(input("Marks in English: "))

Total_marks=m+s+e

avg=Total_marks/3

print(f"Total marks: {Total_marks}"'\n'f"Average Marks: {avg}")

if(avg>90):
  print("A")

elif(avg>80 and avg<=90):
  print('B')

elif(avg>70 and avg<=80):
  print('C')

elif(avg<70):
  print("passs")