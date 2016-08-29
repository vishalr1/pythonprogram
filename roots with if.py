x=input("Enter a value for a:")
a=float(x)
x=input("Enter a value for b:")
b=float(x)
x=input("Enter a value for c:")
c=float(x)
d=(b**2)-4*a*c
e=d**0.5
f=2*a

if(d>=0):
    r1=(-b+d)/e
    r2=(-b-d)/e
    print("Roots are: ",r1,"  ",r2)
else:
    print("Value of b^2-4ac is negative. Roots cannot be calculated")
