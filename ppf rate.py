x=input("Enter age: ")
age=int(x)
x=input("Enter amount(in lakhs): Rs.")
amt=int(x)
if age<60 :
    if amt<500000 :
        print("Your PPF interest rate = 6%")

    elif amt<1000000 :
        print("Your PPF interest rate = 8%")

    elif amt>=1000000 :
        print("Your PPF interest rate = 10%")

if age>=60 :
    if amt<500000 :
        print("Your PPF interest rate = 8%")

    elif amt<1000000 :
        print("Your PPF interest rate = 9%")

    elif amt>=1000000 :
        print("Your PPF interest rate = 11%")
print("press enter to continue")
