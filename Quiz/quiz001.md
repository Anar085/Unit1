# Quiz 001

## Paper solution
[IMG_0168](https://github.com/user-attachments/assets/f1317451-f9d1-4d29-b5a5-2b976f27fd34)

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
![ima](https://github.com/user-attachments/assets/1a2261d2-7d5f-43c9-b8d2-cb2021ca9103)


## Algorithm flow

![IMG_0175](https://github.com/user-attachments/assets/c77c514b-6cc5-420c-a55e-a6b5fa5f49df)
