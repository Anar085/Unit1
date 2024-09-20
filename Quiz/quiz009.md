# Quiz 009

## Paper solution

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


## Algorithm flow



