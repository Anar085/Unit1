# Quiz 005

## Paper solution
(https://github.com/user-attachments/assets/5bb80aa1-6396-4d84-95e4-b671436dcbc1)

## Code
```.py
msg=input("Enter the message: ")
for letter in msg:
    if letter not in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ -':
        exit("This message is not valid")
alpha="abcdefghijklmnopqrstuvwxyz"
alpha2="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
sum=0
for i in range(len(alpha)):
    if alpha[i] in msg:
        sum+=i+97  #Because of ASCII table
for x in range(len(alpha2)):
    if alpha2[x] in msg:
        sum+=x+65   #Because of ASCII table
print(sum)

```

## Proof of work
(https://github.com/user-attachments/assets/b5f7c9d1-5931-4c25-8c5a-802a2f9b6f85)

## Algorithm flow
