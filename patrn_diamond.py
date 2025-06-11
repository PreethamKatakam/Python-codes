n=int(input("Enter a no."))

for i in range(0,n+1):    
    for j in range(0,n+1):
        if i+j <= n:
            print(" ",end='  ')     #2 spaces for 'end'
        else:
            print("*",end='    ')   #4 spaces for 'end'
    print()

for i in range(n-1,0,-1):    
    for j in range(0,n+1):
        if i+j <= n:
            print(" ",end='  ')     #2 spaces for 'end'
        else:
            print("*",end='    ')   #4 spaces for 'end'
    print()
