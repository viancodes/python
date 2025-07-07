n=int(input("N="))

ans=0

print(f"Multiplication table of {n}:")

for i in range(1,11):
  ans=n*i

  print(f"{n}x{i}={ans}")