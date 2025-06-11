n=int(input("Enter a no."))

for i in range(0,n):    
    for j in range(0,n):
        if i+j <= n:
                print("  ",end=' ')
        for k in range(1,3):            
             if i+j >= n:
                print('*',end=' ')        
    print()

for i in range(n,-1,-1):    
    for j in range(0,n):
        if i+j <= n:
                print("  ",end=' ')
        for k in range(1,3):            
             if i+j >= n:
                print('*',end=' ')        
    print()

'''
for i in range(1,n+1):    
    for j in range(1,n+1):
        for k in range(1,3):
            print(i,j,end=' ')        
    print()
'''
