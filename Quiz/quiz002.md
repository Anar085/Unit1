# Quiz 001

## Paper solution

## Code
```.py
a=int(input("Enter the number of elements in list: "))
ls1=[]
ls2=[]
for x in range(a):
    e=int(input())
    ls1.append(e)
for r in range(a):
    f=int(input())
    ls2.append(f)
for i in range (a):
    if ls1[i]+ls2[i]==20 or ls1[i]==20 or ls2[i]==20:
        print("True")
        break
```

## Proof of work


## Algorithm flow
