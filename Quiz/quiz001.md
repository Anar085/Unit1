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
![image](https://github.com/user-attachments/assets/1a2261d2-7d5f-43c9-b8d2-cb2021ca9103)


## Algorithm flow
(https://github.com/user-attachments/assets/15bf811e-bee4-447e-8d2e-db5ac7ff247b)

