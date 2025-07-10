"""Find All Pairs with a Given Sum

Input: [1, 2, 3, 4, 5], Target = 6

Output: (1, 5), (2, 4)

"""


l1 = list(map(int, input("Enter List: ").split(",")))


n=int(input("Enter target: "))

l1l=len(l1)

for i in range(0, l1l):
  for j in range(i+1, l1l):
    if(l1[i]+l1[j]==n):
      print(f"({l1[i]},{l1[j]})")
