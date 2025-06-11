def Dec_Upper(fun1):
    def wrap(x_name):
        if  ord(x_name[0])>=97 and ord(x_name[0])<=122  :
            print(chr(ord(x_name[0])-32)+x_name[1:])
        else:
            fun1(x_name)
    return wrap

@Dec_Upper
def disp(name):
    print(name)

#call
a=input("Enter the name")
disp(a)
