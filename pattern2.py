i=1
n=int(input("Enter  the no. :"))

#prints only odd pattern
while i<=n:
    j=1
    while j<=i:
        if i%2==0:
            pass
        else:
            print("*",end=' ')
        j=j+1
    i=i+1    
    if i%2==0:
        pass  #used to not add extra line for i=even
    else:
        print("")
