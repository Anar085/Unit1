# Quiz 006

## Paper solution
(https://github.com/user-attachments/assets/ed2b6634-c61e-4326-b2b9-35e252ecad94)

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
        num1=random.randint(0,73)
        result+=str(symbols[num1])
print(result)

```

## Proof of work


## Algorithm flow
