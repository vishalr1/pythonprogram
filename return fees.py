x=input("Enter Fees paid: ")
fees = int(x)
x=input("After how many days: ")
days = int(x)
if(days<=5):
    amt=fees-(fees*0.1)
    print("Deduction rate=10%")
elif(days<=10):
    amt=fees-(fees*0.15)
    print("Deduction rate=15%")
elif(days<=15):
    amt=fees-(fees*0.2)
    print("Deduction rate=20%")
elif(days>15):
    amt=fees-(fees*0.3)
    print("Deduction rate=30%")
print("You will get Rs.",amt)
