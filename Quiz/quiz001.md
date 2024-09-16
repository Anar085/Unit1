# Quiz 001

## Paper solution
![IMG_0168](https://github.com/user-attachments/assets/f1317451-f9d1-4d29-b5a5-2b976f27fd34)

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
(https://github.com/user-attachments/assets/15bf811e-bee4-447e-8d2e-db5ac7ff247b)

