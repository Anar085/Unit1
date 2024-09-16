# Quiz 009

## Paper solution

## Code
```.py

def encryption(msg:str, shift:int):
    shift=shift%26
    alp="abcdefghijklmnopqrstuvwxyz"
    alp2="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in range(len(msg)):
        p=0
        for x in range(len(alp)):
            if msg[i]==alp[x]:
                p=x+1
        if shift>=0:
            u=(p + shift) % 26 - 1
            msg[i]=alp[u]
        else:
            shift=shift+26
            u=(p + shift) % 26 - 1
            msg[i]=alp[u]

    for r in range(len(msg)):
        p = 0
        for y in range(len(alp)):
            if msg[r] == alp2[y]:
                p = y + 1
        if shift >= 0:
            d=(p + shift) % 26 - 1
            msg[r] = alp2[d]
        else:
            shift = shift + 26
            d=(p + shift) % 26 - 1
            msg[r] = alp2[d]
    return msg
m=encryption(msg="aaaaA", shift=4)
print(m)


```

## Proof of work


## Algorithm flow



