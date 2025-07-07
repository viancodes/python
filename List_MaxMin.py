l=list(map(int, input().split(",")))
maxi=l[0]
mini=l[0]
for i in l:
  if i>maxi:
    maxi=i

  if i<mini:
    mini=i


print(maxi,mini)























# l=[]

# l=list(map(int, input().split(",")))

# l.sort()


# l_max=max(l)
# l_min=min(l)

# print(l[-1])
# print(l[0])

# print(l_max, l_min)