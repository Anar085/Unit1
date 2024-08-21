# Quiz 001

## Paper solution

## Code
'''.py
n=input()
n=str(n)
lst=n.split()
for i in lst:
    lst1=list(i)
    s=len(i)
    x=s-2
    a=str(x)
    ans=lst1[0]+a+lst1[s-1]
    print (ans, end=" ")


'''

## Proof of work
