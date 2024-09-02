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
