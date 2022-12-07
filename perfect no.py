num=int(input())
lst=[]
for i in range(1,num//2+1):
    if num%i==0:
        lst.append(i)
if sum(lst)==num:
    print('perfect number')
else:
    print("not perfect number")