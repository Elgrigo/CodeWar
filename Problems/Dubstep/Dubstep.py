def song_decoder(song):
    song1=str()
    t=0
    x=0
    n=len(song)
    if n<3:
        print(song)
    else:
        while x<n:
            if song[x]!="W":
                song1=song1+song[x]
                x+=1
            else:
                while True:
                    if song[x:x+3]=="WUB":
                        x=x+3
                        t+=1
                    else:
                        break
                print(t)
                if t==0:
                    song1=song1+song[x]
                else:
                    song1=song1+" "
                    t=0
        if(song1[0]==" "):
            song1=song1[1:]
        n=len(song1)
        if(song1[n-1]==" "):
            song1=song1[:n-1]
        return song1
n=song_decoder("AWUBBWUBC")
print(n)

        