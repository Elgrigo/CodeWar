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
print(balanced_parens(1))
print(balanced_parens(2))
print(balanced_parens(3))
print(balanced_parens(4))

"""def rec(c,s):    
    if len(s) == 2 * c:
        x=0
        y=0
        for i in s:
            if i == '(':
                x += 1
            if i == ')':
                y += 1
            if x < y:
                break
        if(x == y):
            yield s
        return s[:-1]
    else:
        rec(c,s+'(')
        rec(c,s+')')"""


