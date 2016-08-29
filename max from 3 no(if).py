x=input("Enter a:")
a=int(x)
x=input("Enter b:")
b=int(x)
x=input("Enter c:")
c=int(x)
if(a>b and a>c):
    print("a is max")
elif(b>a and b>c):
    print("b is max")
elif(a==b and b==c):
    print("All are equal")
elif(a==b and a>c):
    print("a and b are equal and max")
elif(a==c and a>b):
    print("a and c are equal and max")
elif(b==c and c>a):
    print("b and c are equal and max")

else:
    print("c is max")
x=input("Press enter to continue")
