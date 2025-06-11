n=int (input ("Enter a no.: "))
pat=int (n/2+1)


# I pattern
print("I pattern :")
for i in range (1,n+1) :
    for j in range (1,n+1):
        if i==1 or j==n or i==n or j==n:
            print ('*',end='    ')
        else:
            print (" ",end='  ')
    print ()
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


#S pattern
print("S pattern :")
for i in range (1,n+1):
    for j in range (1,n+1):
        if i==1 or (i<=pat and j==1) or i==pat or i==n or (i>=pat and j==n):
            print (' * ',end='')
        else:
            print (" ",end='   ')
    print()
print()
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


#X pattern
print("X pattern :")
for i in range (1,n+1):
    for j in range(1,n+1):
        if i+j==n+1 or i==j:
            print("*",end='    ')
        else:
            print(" ",end='    ')
    print()
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
