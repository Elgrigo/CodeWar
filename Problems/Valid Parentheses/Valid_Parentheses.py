def valid_parentheses(string):
    x,y=0
    for i in string:
        if i == '(':
            x += 1
        if i == ')':
            y += 1
        if x < y:
            return(False)
    if(x != y):
        return(False)
    else:
        return(True)

