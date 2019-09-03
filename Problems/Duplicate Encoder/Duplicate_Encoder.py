def duplicate_encode(word):
    word=word.lower()
    word1=word
    n=len(word)
    j=0
    word2=str()
    for i in range(n):
        if word[i]==word1[j]:
            if word.count(word[i])==0:
                word2+='('
                j+=1
            else:
                word2+=')'
                word1.replace(word[i], '')
                j+=1
        else:
            word1+=')'
    return word2
#x="Ssd"
#n=duplicate_encode(x)
#print(n)