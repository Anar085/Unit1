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
        sum+=i+97
for x in range(len(alpha2)):
    if alpha2[x] in msg:
        sum+=x+65
print(sum)




```

## Proof of work


## Algorithm flow
