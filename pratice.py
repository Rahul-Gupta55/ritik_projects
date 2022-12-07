# age=int(input("Enter a number: "))
# if age>18:
#     print("Yes")
# else:
#    print("No")    

# text=input("Enter the text\n")

# if("make money" in text):
#     spam=True
# elif("subscribe now" in text):
#     spam=True
# elif("play now" in text):
#     spam=True
# else:
#     spam=False

# if(spam):
#      print("This text is spam")
# else:
#     print("This text is not spam") 
# 
# 
#
# names=["Rahul","shorab","Gorav","Hemant"]
# name=input("Enter your name to check \n")

# if name in names:
#     print("Your name is present in the list")
# else:
#     print("Your name is not present")    


# marks=int(input("Enter a number \n"))

# if marks>=90:
#     Grade="A"    
# elif marks>=80:
#     Grade="B"  
# elif marks>=70:
#     Grade="C"  
# elif marks>=60:
#     Grade="D"    
# elif marks>=50:
#     Grade="E"    
# else:
#     Grade="F"
# print("Your grade is " + Grade) 
# 
#    
# i=1
# while i<=50:
#     print(i)
#     i=i+1

# fruits=["apple","banana","Mango","watermelon"]
# print(len(fruits))
# i=0
# while i<len(fruits):
#     print(fruits[i])
#     i=i+1

# for i in range(1,10):
#     print(i)

# num=int(input("Enter a number:"))
# for i in range(1,11):
#     # print(str(num) + "X" + str(i) + "=" + str(i*num)
#     print(f"{num} X {i}={num*i}")


# a=["Hitesh","Sachin","Rohan","Sehwag"]

# for name in a:
#     if name.startswith("S"):
#         print("Hello"+ name)

# num=int(input("Enter a number:"))
# prime="True"

# for i in range(2,num):
#     if (num%i==0):
#         prime=False
#         break
# if prime:
#     print("this number is prime number")
# else:
#     print("This number is not a prime number")


#------Program to find prime number------
# num=int(input("Enter a number:"))
# Prime=True
# for i in range(2,num):
#     if num%i==0:
#         prime=False
#         break

# if Prime:
#     print("This number is prime number")
# else:
#     print("This number is not prime number")

#-------Program to find factorial--------
# num=int(input("Enter a number :")) 
# factorial =1
# for i in range(1,num+1):
#     factorial=factorial*i
# print(f"The factorial of {num} is {factorial}") 


#------Program to find sum of n natural number
# num=int(input("Enter a number:"))
# sum=0
# for i in range(0,num+1):
#     sum=sum+i
# print(f"The sum of given {num} is {sum}")  


#-------Making triangel of star-------

# for i in range(8):
#     print("*" * (i+1))

# n=5
# for i in range(5):
#     print(" " * (n-i-1),end="")
#     print("*" * (2*i+1),end="")
#     print(" " * (n-i-1))
    

#------To calculate percentage by marks

# marks=[44,55,66,77]
# percentage1=(sum(marks)/400)
#  * 100

# marks=[33,44,55,66]
# percentage2=(sum(marks)/400) *100

# print(percentage1)
# print(percentage2)

# def percent(marks):
#     p=sum(marks)/400*100
#     return p

# marks=[33,44,55,66]
# percentage1=percent(marks)

# marks=[44,55,66,77]
# percentage2=percent(marks)

# print(percentage1)
# print(percentage2)     



#-------To find maximum of three numbers-----
# def maximum(num1,num2,num3):
#     if(num1>num2):
#         if num1>num3:
#             return num1
#         else:
#             return num3
#     else:
#         if(num2>num3):
#             return num2
#         else:
#             return num3

# m=maximum(34,56,78)
# print("The value of maximum is" +str(m))   


#------program to convert celsius to fahrenhite

# def fahr(cel):
#     return (cel*(9/5)+32)
# c=0        
# f=fahr(c)
# print("Fahrenhite temperature is "+ str(f))  


#-------Program to calculate sum of natural number by recursive function

# def sum_recursive(n):
#     if n==0:
#         return 0
#     return n + sum_recursive(n-1)
# f=sum_recursive(5)
# print(f)        
    

#-------To print star(*) n times

# n=5
# for i in range(n):
#     print("*" * (n-i))    
                      
a=3
b=10
print(a%b)                      

          
    