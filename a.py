import math
n= int (input())
for _ in range(n):
    a=int(input())
    if a%5!=0:
        print (-1)
    else:
        b=int(a/10)
        c=a%10
        if c==5:
            print(b+1)
        else:
            print(b)