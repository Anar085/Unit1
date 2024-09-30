# Quiz 005

## Paper solution
![IMG_0266](https://github.com/user-attachments/assets/d864f0e8-f175-4e35-a983-f55205837e1d)


## Code
```.py
def letterchange(msg:str):
    dic={"a":"4",
         "e":"3",
         "i":"1",
         "o":"0",
         " ":"_"}
    outmsg=""
    for letter in msg:
        if letter in dic:
            outmsg+=dic[letter]
        else:
            outmsg+=letter
    return outmsg
m=letterchange(msg="Hello world")
print(m)

```

## Proof of work


![SCquiz 16](https://github.com/user-attachments/assets/104ca583-25c2-4f75-929a-4058c84a7491)


## Algorithm flow



