# Quiz 015

## Paper solution

## Code
```.py

def averagelength(words: list):
    lengths = []
    for word in words:
        l=0

        alp="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        for letter in word:
            if letter in alp:
                l+=1
        lengths.append(l)
    sum=0
    for l in lengths:
        sum+=l
    average=sum/len(words)
    average=round(average,1)
    return average

words=["Computer Science","Art"]
m=averagelength(words)
print(f"Average length is {m}, if spaces are not counted")

```

## Proof of work

![image](https://github.com/user-attachments/assets/e40554e1-3059-44a3-adc1-4cf0d0a960aa)

## Algorithm flow
![image](https://github.com/user-attachments/assets/3c2b09e6-480f-41fd-a620-810586e0b5a2)





