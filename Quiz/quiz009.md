# Quiz 009

## Paper solution
![IMG_0276](https://github.com/user-attachments/assets/8e320f55-fb85-4a32-ae6d-6cbaec850e11)

## Code
```.py
def encryption(msg: str, shift: int):
    shift = shift % 26
    alp = "abcdefghijklmnopqrstuvwxyz"
    alp2 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alp=list(alp)
    alp2=list(alp2)

    msgout = []
    for char in msg:
        if char in alp:
            index = alp.index(char)
            p = (index + shift) % 26
            msgout.append(alp[p])
        elif char.isupper():
            index = alp2.index(char)
            p = (index + shift) % 26
            msgout.append(alp2[p])
        else:
            msgout.append(char)

    return msgout
msgout = encryption(msg="aaaA", shift=-1)
output=""
for y in range(len(msgout)):
    output+=msgout[y]
print(output)

```

## Proof of work
![image](https://github.com/user-attachments/assets/0051d832-43cd-4b54-8696-8901d20d1513)


## Algorithm flow

![image](https://github.com/user-attachments/assets/b5829c40-c70b-4b16-82d3-f987dfb8c207)


