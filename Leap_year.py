x=int(input("Enter year: "))


if(x%4==0 and x%100!=0) or (x%400==0):
    print(f"{x} is leap year")

#hi

else:

  print(f"{x} is not a leap year")
