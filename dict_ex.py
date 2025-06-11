d={'a':1,'b':2,'c':3}
print(d)
print(d.items())
print(d.keys())
print(d.values())


#printing individual item in the dict
for k,v in d.items():
    print(k,v)
    #(or)
for i in d.items():
    print(i[0],i[1])

#dict updation
d.update({'d':4})
print(d)
d.update({'d':None})
print(d)
print(d.get('d'))

#usage of from keys , i.e, creating a dict using a list
a=[1,2,3]
print(a)
d1=dict.fromkeys(a,0)
print(d1)

a1=[1,2,3]
print(a1)
b1=[]
for i in a1:
    b1.append(i**2+2.6/3)
print(b1)
d2=dict.fromkeys(a1,b1)
print(d1)

#update all values of the dicts to the squares of the keys 
for k,v in d1.items():
    d1.update({k:k**2})    
print(d1)












