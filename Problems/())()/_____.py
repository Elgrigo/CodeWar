def astvac_giti(n):
    y=1
    s=str()
    while y<=2**n:
        y+=1
        if len(s) == 2*n:
            x,y = 0
            for i in s:
                if i == '(':
                    x += 1
                if i == ')':
                    y += 1
                if x < y:
                    s=""
                    break
            if(x != y):
                s=""
            else:
                l.append(s)
                s=''
        if len(s)< 2 * n:
            s+="("
            astvac_giti(n)
        if len(s)< 2 * n:
            s+=")"
            astvac_giti(n)
    return(l)
n=astvac_giti(2)
print(n)
