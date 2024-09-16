# Quiz 004

## Paper solution
![IMG_0171](https://github.com/user-attachments/assets/44d93e0e-ec85-4445-b189-eeeac0c705ec)

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
![quiz 4 sc](https://github.com/user-attachments/assets/de9d0622-0d32-4fb8-a4b2-8e37f099ece3)


## Algorithm flow
![IMG_0178](https://github.com/user-attachments/assets/f08f3370-0369-4f25-9f89-c29f4dcf7e34)
