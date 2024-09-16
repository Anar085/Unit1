# Quiz 003

## Paper solution
![IMG_0170](https://github.com/user-attachments/assets/81f4a676-8c27-423a-8295-c5ef8420ae14)

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
![Quiz 3 sc](https://github.com/user-attachments/assets/2a9daab3-972f-4d03-a07f-0bf7eaf56714)

## Algorithm flow
https://lucid.app/lucidchart/a9661a2f-b861-4566-90b5-6248f784fc01/edit?viewport_loc=-730%2C-190%2C4661%2C2156%2C0_0&invitationId=inv_b4a22120-f936-4075-b542-b0f98dacd86f
