# Quiz 001

## Paper solution
(https://github.com/user-attachments/assets/575d789b-f4c1-46c8-89ec-afabfd2fad08)

## Code
```.py
n=input("Enter the input: ")
lst=n.split()
for i in lst:
    if len(i)==1:
        print(i, end=" ")
    else:
        lst1=list(i)
        s=len(i)
        x=s-2
        a=str(x)
        ans=lst1[0]+a+lst1[s-1]
        print (ans, end=" ")




```

## Proof of work
(https://github.com/user-attachments/assets/5b46bbba-2987-487a-a73d-ca42989f54a2)


## Algorithm flow

