sum=0
count=0
while(1==1):
    x=int(input("Enter a no.:"))
    sum=sum+x
    count=count+1
    ans=input("Continue(y/n):")
    if(ans=='n'):
        break
avg=sum/count
print(avg)
