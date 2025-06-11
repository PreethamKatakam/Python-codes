
import sys
print(sys.argv[0])

#print(sum(int(sys.argv[1:]))) ----> doesn't work as we have to individually conert the str args  to int values
sum=0
for i in sys.argv[1:]:
    sum+=int(i)
print(sum)

s1=0
for i in range(int(sys.argv[-1])):
    s1=s1+i
print(s1)
