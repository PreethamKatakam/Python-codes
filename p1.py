#replacling space with given character in the text

def repl(txt,ch):
    op=''
    for i in txt:
        if i == ' ':
            i=ch
        op=op+i
    return op

#calling
a=input("Enter any text including spaces: ")
b=input("Enter the character to be filled in the space: ")
res=repl(a,b)
print("The output is :",res)
