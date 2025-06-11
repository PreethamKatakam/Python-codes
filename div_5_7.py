c=0
for i in range(1,1001):
    if i%5==0 and i%7==0:
        print(i,'is divisible')
        c=c+1

print("Total no.s divisible: ",c)
