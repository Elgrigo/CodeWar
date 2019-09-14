def decodeMorse(morse_code):
    d = {'.-': "A", '-...': "B", '-.-.': "C", '-..': 'D', '.': 'E', '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P', '--.-': 'Q','...---...':'SOS', '.-.': 'R', '...': 'S', '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y', '--..': 'Z','-.-.--':'!','.-.-.-':'.'}
    #return " ".join(''.join([[d[x] for x in morse.split()] for morse in morse_code.split('   ')]))
    #morse=list()
    print([[d[x] for x in morse.split()] for morse in morse_code.split('   ')])
    return " ".join([''.join([d[x] for x in morse.split()]) for morse in morse_code.split('   ')])
    """list1=morse_code.split("   ")
    for x in range(len(list1)):
        list1[x]=list1[x].split()
    for x in range(len(list1)):
    for y in range(len(list1[x])):
        list1[x][y]=d[list1[x][y]]
    for x in range(len(list1)):
        list1[x]="".join(list1[x])
    morse_code=" ".join(list1).strip()
    return(morse_code)"""
    
n=decodeMorse('...---... -.-.--   - .... .   --.- ..- .. -.-. -.-   -... .-. --- .-- -.   ..-. --- -..-   .--- ..- -- .--. ...   --- ...- . .-.   - .... .   .-.. .- --.. -.--   -.. --- --. .-.-.-')
print(n)
