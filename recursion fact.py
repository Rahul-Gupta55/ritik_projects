
def recurfact(n):
    if n==1:
        return n
    return n*recurfact(n-1)
m=int(input("Enter a number: "))
if m<1:
    print("no factorial")
else:
    print(recurfact(m)) 



# def factorial_recursive(n):
#     if n==0 or  n==1:
#         return 1
#     return n * factorial_recursive(n-1)

# f=factorial_recursive(4)
# print(f)            