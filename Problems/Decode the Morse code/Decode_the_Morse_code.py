def decodeMorse(morse_code):
    while True:
        if morse_code[0]==" ":
            morse_code=morse_code[1:]
        else:
            break
    while True:
        if morse_code[-1]==" ":
            morse_code=morse_code[:-1]
        else:
            break
    morse_code=" "+morse_code+" "
    morse_code=morse_code.replace("  "," / ")
    morse_code=morse_code.replace(" ","  ")
    d = {' .- ': "A", ' -... ': "B", ' -.-. ': "C", ' -.. ': 'D', ' . ': 'E', ' ..-. ': 'F', ' --. ': 'G', ' .... ': 'H', ' .. ': 'I', ' .--- ': 'J', ' -.- ': 'K', ' .-.. ': 'L', ' -- ': 'M', ' -. ': 'N', ' --- ': 'O', ' .--. ': 'P', ' --.- ': 'Q',' ...---... ':'SOS', ' .-. ': 'R', ' ... ': 'S', ' - ': 'T', ' ..- ': 'U', ' ...- ': 'V', ' .-- ': 'W', ' -..- ': 'X', ' -.-- ': 'Y', ' --.. ': 'Z',' -.-.-- ':'!',' .-.-.- ':'.'}
    for i in d:
        morse_code=morse_code.replace(i," "+d[i]+' ')   
        print(morse_code)
    morse_code=morse_code.replace(" ","")
    morse_code=morse_code.replace("/"," ")
    return morse_code
n=decodeMorse('...---... -.-.--   - .... .   --.- ..- .. -.-. -.-   -... .-. --- .-- -.   ..-. --- -..-   .--- ..- -- .--. ...   --- ...- . .-.   - .... .   .-.. .- --.. -.--   -.. --- --. .-.-.-')
print(n)
