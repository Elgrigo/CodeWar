def balanced_parens(n):
    l = ['()']
    s = set()
    if n == 0:
        return [""]
    elif n == 1:
        return ["()"]
    else:
        for z in range(n - 1):
            for i in l:
                for y in range(len(i)):
                    s.add(i[0:y] + "()" + i[y:])
            l.clear()
            l.extend(s)
            s.clear()
        return l
    

