import math
n=int(input("Enter a number :"))
fact=math.factorial(n)
print(fact)

n1=fact
count=0
print(n1)
    
while int(n1) > 0:
    if(n1%10==0):
        count=count+1
    n1=int(n1/10)
    
for i in str(fact):
    if i == '0':
        count-=1
    
    
print("Count of variables :",count)

