# Quiz 008

## Paper solution
![IMG_0185](https://github.com/user-attachments/assets/12e08b5d-2c03-4d0b-9ad9-9912819c4342)

## Code
```.py

def hotel(floor: int, room:int, spec:int ):
    lst=[]
    for i in range(1,floor+1):
        for x in range(1,room+1):
           
            num=str(i)+"F"+str(x)
            lst.append(num)
            num=""
    for t in range(floor*room):
        lst[t]="Room "+lst[t]
    return lst[spec-1]
m=hotel(floor=10, room=10, spec=int(input("Enter the room number: ")))
print(m)
```

## Proof of work
![Screenshot 2024-09-13 075648](https://github.com/user-attachments/assets/6b884a52-613b-4e64-9e0f-cf60480f275f)


## Algorithm flow

![IMG_0186](https://github.com/user-attachments/assets/ceca8e27-fb58-4903-b3da-c9fa28aa2aef)

