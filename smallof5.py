print("Enter 5 no.s: ")
n1,n2,n3,n4,n5=int(input()),int(input()),int(input()),int(input()),int(input())

if n1<n2 and n1<n3 and n1<n4 and n1<n5:
    print("n1 is small")
elif n2<n3 and n2<n4 and n2<n5:
    print("n2 is small")
elif n3<n4 and n3<n5:
    print("n3 is small")
elif n4<n5:
    print("n4 is small")
else:
    print("n5 is small")
    
