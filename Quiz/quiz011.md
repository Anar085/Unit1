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
        "January": (31, 0),
        "February": (28, 1),
        "March": (31, 3),
        "April": (30, 0),
        "May": (31, 1),
        "June": (30, 4),
        "July": (31, 0),
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
![image](https://github.com/user-attachments/assets/04efb13b-79e7-4f63-bd94-f27b064bfcd7)


## Algorithm flow




