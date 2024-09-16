# Quiz 005

## Paper solution


![IMG_0172](https://github.com/user-attachments/assets/c3fc4efd-0c12-44e7-9854-5db954195743)

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


![quiz 5 sc](https://github.com/user-attachments/assets/e098faa2-9f3a-4127-94cb-9f2bd0d7e7f9)


## Algorithm flow


![IMG_0179](https://github.com/user-attachments/assets/76eaf8b8-e9bb-48e8-b806-06ccc43f212a)

