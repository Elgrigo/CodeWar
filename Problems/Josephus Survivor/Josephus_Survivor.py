def josephus_survivor(n,k):
    a=list()
    a.append(" ")
    for i in range(1,n+1):
        a.append(i)
    print (a)
    x=0
    x1=-1
    y=0
    for i in range(1,n):
        x+=k
        if x%n!=0:
            x%=n
        else:
            x=n
        a.remove(a[x])
        x-=1
        n-=1
    return int(a[1])
n=josephus_survivor(100,1)
print(n)

