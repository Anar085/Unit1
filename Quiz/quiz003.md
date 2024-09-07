# Quiz 003

## Paper solution
(https://github.com/user-attachments/assets/4beddb39-1973-428e-9038-d7f876a22105)

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
https://lucid.app/lucidchart/a9661a2f-b861-4566-90b5-6248f784fc01/edit?viewport_loc=-730%2C-190%2C4661%2C2156%2C0_0&invitationId=inv_b4a22120-f936-4075-b542-b0f98dacd86f
