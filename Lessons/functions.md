## MB4
```.py
def mystery_box4(scores):
    scores=[]
    while True:
        score=int(input())
        if score==0:
            break
        scores.append(score)
    vscores=[]
    for score in scores:
        if score in range(1,8):
            vscores.append(score)
    s=0
    for i in vscores:
        s=s+i
    if len(vscores)!=0:
        aver=s//len(vscores)
    else:
        aver=0
    return aver
n=mystery_box4(scores="Enter the scores")
print(n)
```
## MB 2
```.py
def mystery_box2(msg):
    msg=input("Enter your email: ")
    name=""
    s=len(msg)
    for i in range(s):
        if msg[i]==".":
            break
        name=name+msg[i]
    x=len(name)
    surname=""
    for i in range(x+1,s):
        if msg[i]=="@":
            break
        surname=surname+msg[i]
    r=len(surname)
    domain=""
    for i in range(x+r+2,s):
        domain=domain+msg[i]
    output=name+" "+ surname+" "+domain
    return output
n=mystery_box2(msg="Enter your email: ")
print(n)

```
## MB1
```.py
def mystery_box1(msg, cond):
    word=input(msg)
    cond=bool(input())
    s=len(word)
    if cond is False:
        output=''
        for i in range(s-1,-1,-1):
            output.append(word[i])
    else:
        ls1='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        ls2='abcdefghiklmnopqrstuvwxyz'
        for x in range (26):
            if ls1[x] in word:
                word[x]=ls2[x]
        output=''
        for r in range(s-1,-1,-1):
            output.append(word[r])
    return output
n= mystery_box1(msg="Enter the message",cond="Enter True/False")
print(n)
```
## MB3
```.py
def mystery_box3(lst):
    lst=[]
    for i in range(3):
        x=int(input())
        lst.append(x)
    factors1=[]
    for j in range (2,lst[0]+1):
        for h in range(2,j+1):
            if j%h!=0
        if lst[0]%j==0:
            factors1.append(j)
    factors2=[]
    for p in range (2,lst[1]+1):
        if lst[1]%p==0:
            factors2.append(p)
    factors3=[]
    for z in range (2,lst[2]+1):
        if lst[2]%z==0:
            factors3.append(z)
    comdiv=[]
    for div in factors1:
        if div not in factors2 and  factors3:
            comdiv.append(div)
    for div in factors2:
        if div not in factors1 and  factors3:
            comdiv.append(div)
    for div in factors3:
        if div not in factors2 and not factors1:
            comdiv.append(div)
    p=1
    for g in range(len(comdiv)):
        p=p*comdiv[g]
    for k in range(len(comdiv)):
        if comdiv[k]%comdiv[k+1]:
            del comdiv[k+1]
    return comdiv

    
n=mystery_box3(lst="Enter the list: ")
print(n)
```

