# Quiz 004

## Paper solution

## Code
```.py
n=int(input())
ls=[]
for i in range(1,n):
    if n%i==0:
        ls.append(i)
s=0
for i in ls:
    s=s+i
if s==n:
    ls.append(True)
    print(ls)
else:
    print(ls)

```

## Proof of work


## Algorithm flow
