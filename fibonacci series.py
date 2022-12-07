n=int(input("Enter a number :"))
sum=0
temp=1
if n==0:
    print(0)
else:
    print(sum)
    print(temp)    
for i in range(2,n):
    d=sum+temp
    sum=temp
    temp=d
    print(d)        
