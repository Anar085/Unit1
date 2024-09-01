# Quiz 003

## Paper solution

## Code
```.py
in_pro=input("Enter DNA chain: ")
for str in in_pro:
    if str not in 'ATGC':
        exit(1)
for i in in_pro:
    if i=="A":
        print("T", end="")
    if i=="T":
        print("A",end="")
    if i=="C":
        print("G", end="")
    if i=="G":
        print("C", end="")
    

```

## Proof of work


## Algorithm flow
