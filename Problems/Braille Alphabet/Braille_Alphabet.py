d = {'a': '.     ', 'b': '. .   ' , 'c' : '..    ', 'd': '.. .  ', 'e': '.  .  ', 'f': '...   ','g': '....  ', 'h': '. ..  ','i':' ..   ', 'j': ' ...  ', 'k': '.   . ', 'l': '. . . ', 'm': '..  . ', 'n': '.. .. ', 'o': '.  .. ', 'p': '... . ', 'q': '..... ','r': '. ... ', 's': ' .. . ', 't': ' .... ', 'u': '.   ..', 'v': '. . ..', 'w': ' ... .', 'x': '..  ..', 'y': '.. ...', 'z': '.  ...','!':'  ... ','.':'  .. .',' ':'      ','?':'  . ..','1': '.     ', '2': '. .   ' , '3' : '..    ', '4': '.. .  ', '5': '.  .  ', '6': '...   ','7': '....  ', '8': '. ..  ', '9':' ..   ', '0': ' ...  '}
s = input("Your string:")
k=0
list2=list()
list1 = list()
for i in s:
    list1.append(i)
if list1[0].isdigit():
    list2.append(' . ...'+d[list1[0]])
else:
    if list1[0].isupper():
        list1[0]=list1[0].lower()
        list2.append('   . .     .'+d[list1[0]])
    else:
        list2.append(' . ...'+d[list1[0]])
for i in range(1,len(list1)):
    if list1[i].isdigit():   
        if list1[i-1].isdigit()==True:
            list2.append(d[list1[i]])
            k+=1
        else:
            list2.append(' . ...'+d[list1[i]])
    else:
        if not list1[i-1].isdigit():
            if list1[i].isupper():
                list1[i]=list1[i].lower()
                list2.append('     .'+d[list1[i]])
            else:
                list2.append(d[list1[i]])
        else:
            if list1[i].isupper():
                list1[i]=list1[i].lower()
                list2.append('   . .     .'+d[list1[i]])
            else:
                list2.append('   . .'+d[list1[i]])
s = str("".join(list2)) 
print(s)