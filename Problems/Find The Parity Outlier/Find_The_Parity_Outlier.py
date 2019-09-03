def find_outlier(integers):
    n=len(integers)
    k=0
    if integers[0]%2==0 and integers[1]%2==0 or integers[0]%2==0 and integers[2]%2==0 or integers[2]%2==0 and integers[1]%2==0:
        k+=1
    if k>0:
        for i in range(n):
            if(integers[i]%2==1):
               # return k
                return integers[i]
                break
    else:
        for i in range(n):
            if(integers[i]%2==0):
                return integers[i]
                break