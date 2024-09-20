# Quiz 011

## Paper solution

## Code
```.py

def calendar(month: str):
    all_months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
                  "November", "December"]
    week_days = ["Mo", "Tu", "We", "Th", "Fr", "Sa", "Su"]
    if month not in all_months:
        print("Invalid month")
    if month == "January":
        for i in range(1, 32):
            t = i % 7
            print(i, week_days[t - 1], end=" ")
    elif month == "February":
        for i in range(1, 30):
            t = i % 7
            t=(t+1)%7
            print(i, week_days[t ], end=" ")
    elif month == "March":
        for i in range(1, 32):
            t = i % 7
            t = (t + 3) % 7
            print(i, week_days[t ], end=" ")
    elif month == "April":
        for i in range(1, 31):
            t = i % 7
            print(i, week_days[t-1 ], end=" ")
    elif month == "May":
        for i in range(1, 32):
            t = i % 7
            t = (t + 1) % 7
            print(i, week_days[t ], end=" ")
    elif month == "June":
        for i in range(1, 31):
            t = i % 7
            t = (t + 4) % 7
            print(i, week_days[t], end=" ")
    elif month == "July":
        for i in range(1, 32):
            t = i % 7

            print(i, week_days[t -1], end=" ")
    elif month == "August":
        for i in range(1, 32):
            t = i % 7
            t = (t + 2) % 7
            print(i, week_days[t - 1], end=" ")
    elif month == "September":
        for i in range(1, 31):
            t = i % 7
            t = (t + 5) % 7
            print(i, week_days[t - 1], end=" ")
    elif month == "October":
        for i in range(1, 32):
            t = i % 7
            print(i, week_days[t ], end=" ")
    elif month == "November":
        for i in range(1, 31):
            t = i % 7
            t = (t + 3) % 7
            print(i, week_days[t - 1], end=" ")
    elif month == "December":
        for i in range(1, 32):
            t = i % 7
            t = (t + 5) % 7
            print(i, week_days[t - 1], end=" ")
month=input("Enter the month")
c=calendar(month)
print(c)





```

## Proof of work
![image](https://github.com/user-attachments/assets/97b01069-55aa-4c40-8f69-487d2900e468)


## Algorithm flow




