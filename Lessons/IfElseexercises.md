# Questions
1.Create a program that organizes from largest to smallest three heights in cms entered by the user.
2.Create a program that calculates the tax for a salary entered by the user following the table below
3.Write a program to sort alphabetically three names entered by the user. Note: Assume that only the first letter of names are the same. 
4.Create a program that calculates the median for a series of scores entered by the user. The user enters either 4 or 5 scores.


## Codes
1.
```.py

      h1,h2,h3=map(int,input().split())
      m=max(h1,h2,h3)
      n=min(h1,h2,h3)
      l=h1+h2+h3-m-n
      print(m,l,n)
```

2.
```.py

      salary=int(input("Enter your salary: "))
      if salary>=0 and salary<=10000:
      print(salary/20)
      if salary>=10001 and salary<=50000:
          print(salary/10)
      if salary>=50001 and salary<=100000:
          print(salary*0.15)
      if salary>100000:
          print(salary/4)
```
3.
```.py

    a,b,c=map(str,input("Enter names: ").split())
    if a[0]==b[0] and b[0]==c[0]:
          if a[1]>b[1] and a[1]>c[1] and b[1]>c[1]:
                print(c,b,a)
          if a[1]>b[1] and a[1]>c[1] and b[1]<c[1]:
                print(b,c,a)
          if b[1]>a[1] and b[1]>c[1] and a[1]>c[1]:
                print(c,a,b)
          if b[1]>a[1] and b[1]>c[1] and a[1]<c[1]:
                print(a,c,b)
          if c[1]>a[1] and c[1]>b[1] and a[1]>b[1]:
                print(b,a,c)
          if c[1]>a[1] and c[1]>b[1] and a[1]>b[1]:
                print(a,b,c)
    if a[0]==b[0] and b[0]>c[0]:
          print(c,a,b)
    if a[0]==b[0] and b[0]<c[0]:
          print(a,b,c)
    if a[0]==c[0] and b[0]>c[0]:
          print(c,a,b)
    if a[0]==c[0] and b[0]<c[0]:
          print(b,c,a)
    if c[0]==b[0] and a[0]>c[0]:
          print(c,b,a)
    if c[0]==b[0] and a[0]<c[0]:
          print(a,c,b)
```

4.
```.py

      lst = []
      num= int(input("Enter number of scores : "))
      for i in range(num):
          sc= int(input())
          lst.append(sc)
      lst.sort()
      if num==4:
          print ("median:",lst[1]/2+lst[2]/2)
      if num==5:
          print ("median:",lst[2])

```
