# Quiz 008

## Paper solution

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


## Algorithm flow


