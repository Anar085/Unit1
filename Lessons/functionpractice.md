```.py
def practice(a:int,b:int):
    output=(a**2+b**2)*0.5
    return output
m=practice(a=3,b=4)
print(m)
```

```.py
def practice(a:int,b:int, c:int):
    if a+b+c==180:
        return True
    else:
        return False
m=practice(a=30,b=40,c=110)
print(m)

```

```.py
def practice(num:int, base:int):
    lst=[]
    while num!=0:
        d=num%base
        num//=2
        lst.append(d)
    s=len(lst)
    lstout=""
    for i in range (s-1,-1,-1):
        lst[i]=str(lst[i])
        lstout+=lst[i]
    return lstout
m=practice(num=5, base=2)
print(m)

```

```.py
def sum(a:int,b:int):
    output=a+b
    return output
def sumtotal(a:int,b:int,c:int):
    output=sum(a,b)+c
    return output
t=sumtotal(a=4,b=5,c=1)
print(t)

```
