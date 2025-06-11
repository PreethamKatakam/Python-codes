pen=int(input("Enter the no. of pens : "))
book=int(input("Enter the no. of books : "))
tot=(pen*9)+(book*65)
dis=0.15*tot
net=tot-dis
print("The Total bill is:  \t " , tot ,"\nDiscount (15%) is:\t-" , dis , "\n---------------------------------\nNet Bill :  \t\t", net ) 
