prodname=input("enter a product name:")
x=input("Enter quantity:")
q=int(x)
if(prodname=="mobile"):
    print("price is ",q*1000)
elif(prodname=="TV"):
    print("price is ",q*25000)
elif(prodname=="ipod"):
    print("price is ",q*5000)
else:
    print("error")
