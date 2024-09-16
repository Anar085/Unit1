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
![image](https://github.com/user-attachments/assets/e847a2f8-5113-415b-9702-694ec03ac056)

