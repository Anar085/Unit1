# Quiz 002

## Paper solution
![IMG_0169](https://github.com/user-attachments/assets/ea95ccde-4bd9-43ce-95b8-43e08c81893f)

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
![image](https://github.com/user-attachments/assets/6b158931-ac6b-46a0-a232-2ebb4d9b8a19)

## Algorithm flow
(https://github.com/user-attachments/assets/9764bca4-05b2-4e84-a231-324d60205ba5)
