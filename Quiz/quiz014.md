# Quiz 014

## Paper solution
![IMG_0275](https://github.com/user-attachments/assets/8bba2773-1ed2-4a66-87d5-fda3ee334d72)

## Code
```.py

def open_doors(num: int):
    doors = []

    for i in range(0, num):
        doors.append(False)

    for i in range(1, num + 1):
        for j in range(1, num + 1):
            if i % j == 0:
                doors[i - 1] = not doors[i - 1]
    print("Open Doors: ", end='')
    oc=[]
    for i in range(0, num):
        if doors[i]:
            oc.append("Open")
        elif not doors[i]:
            oc.append("Close")
    number=0
    for i in oc:
        if i=="Open":
            number+=1
    return number
m=open_doors(num=10)
print(m)

```

## Proof of work

![image](https://github.com/user-attachments/assets/f3dc3268-f32b-4e73-8f15-d77413b2108a)

## Algorithm flow


![image](https://github.com/user-attachments/assets/1cfcd703-109d-4ddf-b175-ee34bf2a8873)



