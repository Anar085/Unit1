# Quiz 010

## Paper solution
![Image](https://github.com/user-attachments/assets/2ac75edc-fce1-477a-ba89-f35921d2dc1a)

## Code
```.py
def powersTen(msg):
    number=float(msg.split()[0])
    powerlabels = [
        ('Tera', 10 ** 12),
        ('Giga', 10 ** 9),
        ('Mega', 10 ** 6),
        ('kilo', 10 ** 3),
        ('unit', 10 ** 0),
        ('milli', 10 ** -3),
        ('micro', 10 ** -6),
        ('nano', 10 ** -9),
        ('pico', 10 ** -12)
    ]
    result = ""
    for label, value in powerlabels:
        product = number * value
        product_str = f"{product:.12f}"
        while product_str[-1] == '0':
            product_str = product_str[:-1]
        if product_str[-1] == '.':
            product_str = product_str[:-1]
        product_str=list(product_str)
        for i in range(0,len(product_str)-1,4):
            if product_str[i+1] !=".":
                product_str.insert(i + 1, " ")
        product_str="".join(product_str)
        result += f"{product_str} {label}\n"
    result=list(result)
    result.insert(13," ")
    result="".join(result)
    return result.strip()

print(powersTen("5 gram of salt"))




```

## Proof of work

![image](https://github.com/user-attachments/assets/40ddba88-68e4-4ae8-a2eb-24ff084ca469)

## Algorithm flow


![image](https://github.com/user-attachments/assets/d2a4bed7-f910-48ba-9502-75329de4a1be)


