def quadeqn(a,b,c):
  r1=(-b+(((b**2)-(4*a*c))**(1/2)))/(2*a)
  r2=(-b-(((b**2)-(4*a*c))**(1/2)))/(2*a)

  return(r1,r2)

values=input("Enter a,b,c:")


x,y,z=values.split(",")
a=int(x)
b=int(y)
c=int(z)


ans=quadeqn(a,b,c)


print(ans)
