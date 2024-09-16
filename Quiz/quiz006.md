# Quiz 006

## Paper solution
![IMG_0173](https://github.com/user-attachments/assets/c47ec6dc-bec7-4ac6-b228-d31a530a44c2)

## Code
```.py
import random
n=int(input("Enter the length of password: "))
cond=bool(input("Enter True/False: "))
alpha='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
symbols='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!?#%*@$^()'
if cond is False:
    num=random.randint(0,63)
    result=""
    for i in range(n):
        num=random.randint(0,63)
        result+=str(alpha[num])
else:
    result=""
    for i in range(n):
        num1=random.randint(0,72)
        result+=str(symbols[num1])
red="\33[0;31m"
end_code = "\033[00m"

print(f"{red}{result}{end_code}")

```

## Proof of work
(https://github.com/user-attachments/assets/23213974-6832-446c-b318-1f919d70379c)


## Algorithm flow
![IMG_0180](https://github.com/user-attachments/assets/f72bf0b9-d79d-40f0-8008-7a34c559afdb)
