#perfect sq:

p_sq=[]
for i in range(1,101):
    p_sq.append(i**2)
#print(p_sq)
a=int(input("Enter a no. :"))
if a in p_sq:
    print(a,"is a perfect square")
else:
    print(a,"is not a perfect square")



    #(or)
sqr=int(a**0.5)

if (sqr**2)==a:
    print(a,"is a perfect square")
else:
    print(a,"is not a perfect square")
