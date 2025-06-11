n=int (input ("Enter a no.: "))
pat=int (n/2+1)
pat_e=n/2            #for even
print(pat,"-----",pat_e)

for i in range(1,n+1):
    for j in range (1, n+1) :
        if n%2==0:
            if i==pat or j==pat or i==pat_e or j==pat_e:
                print('*', end='     ')
            else:
                print(" ", end='      ')
        else:
            if i==pat or j==pat:
                print('*', end='     ')
            else:
                print(" ", end='      ')
    print()
