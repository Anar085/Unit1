# Quiz 011

## Paper solution

## Code
```.py
def calendar(month: str):
    allmonths = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
                  "November", "December"]
    weekdays = ["Mo", "Tu", "We", "Th", "Fr", "Sa", "Su"]

    if month not in allmonths:
        print("Invalid month")
        return

    months= {
        "January": (31,6),
        "February": (29,2),
        "March": (31, 3),
        "April": (30, 6),
        "May": (31, 1),
        "June": (30, 4),
        "July": (31, 6),
        "August": (31, 2),
        "September": (30, 5),
        "October": (31, 0),
        "November": (30, 3),
        "December": (31, 5)
    }

    daysnumber, firstday = months[month]

    for i in range(1, daysnumber + 1):
        t = (i + firstday) % 7
        print(i,weekdays[t],end=" ")

month = input("Enter the month for calendar: ")
calendar(month)

```

## Proof of work
![image](https://github.com/user-attachments/assets/e0890214-06c3-43a6-b96b-6e5917f908a6)


## Algorithm flow

![image](https://github.com/user-attachments/assets/578ee162-5a92-4629-984c-2d180731bfc1)



