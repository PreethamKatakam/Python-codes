def fun1(x,**y):
    print("X :",x)
    print("Y :",y)
    for i,j in y.items():
        print(i,":",j)

fun1(5,a=10,b=20,c=30)
