# Quiz 002

## Paper solution
(https://github.com/user-attachments/assets/6320722d-2304-4fdc-b451-4a926f7645c2)

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
        print(True)
        break
    else:
        print(False)
        break
```

## Proof of work
(https://github.com/user-attachments/assets/faa5d7d6-eee4-4d7f-9077-dbf12577707f)

## Algorithm flow
