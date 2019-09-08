def buddy(start, limit):
    import math
    a=list()
    for i in range(start, limit+1): 
       a.append(i) 
    sum=0
    sum1=0
    for i in a:
        stop=int(math.sqrt(i))
        for j in range(2, stop+1):
            a1=i/j
            a2=int(a1)
            if a1==a2:
                if j!=i/j:
                    sum+=j+int(i/j)
                else:
                    sum+=j
        stop=int(math.sqrt(sum))
        for j in range(2, stop+1): 
            a1=sum/j
            a2=int(a1)
            if a1==a2:
                if j!=sum/j:
                    sum1+=j+int(sum/j)
                else:
                    sum1+=j
        if sum1==i and i<sum:
            return [i,sum]
        sum1=0
        sum=0
    return ("Nothing")
n=buddy(40, 80)
print(n)