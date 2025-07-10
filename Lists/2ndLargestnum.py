"""Find the Second Largest Number

Input: [1, 5, 3, 9, 7]

Output: 7"""


l1=list(map(int, input("Enter List: ").split(",")))


l1.sort()

print(l1[-2])



"""
l1 = list(map(int, input("Enter List: ").split(",")))

# Remove duplicates
unique = list(set(l1))

# Check if we have at least 2 unique numbers
if len(unique) < 2:
    print("No second largest number")
else:
    unique.sort()
    print(unique[-2])
"""