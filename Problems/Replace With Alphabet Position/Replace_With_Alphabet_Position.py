def alphabet_position(text):
    alp=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    n=len(text)
    text=text.lower()
    text1=str()
    for x in range(n):
        for y in range(26):
            if text[x]==alp[y]:
                text1=text1+str(y+1)+" "
    n=len(text1)
    text1=text1[:n-1]
    return text1


    
