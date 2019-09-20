import json
with open('new_data','r') as json_file:
    data = json.load(json_file)
def search(s):
    k = 0
    l = list()
    for pl in data['people']:
        if pl['name'].count(s) > 0 or pl['phone'].count(s) > 0 or pl['email'].count(s) > 0:
            k+=1
            l.append({"NN":k,"name":pl['name'],"phone":pl['phone'],"email":pl['email']})
    return l
while True:
    print("""Address book manager. Please enter the command to continue:
a - Add new contact
s - Search for contact
e - Edit contact info
r - Remove contact
q - Quit
""")
    print('\n')
    n = input("Your command:")
    if n == 'q':
        print('Good bye ;)')
        break
    elif n == 'a':
        print('Please, fill following information:')
        name = input("Name:")
        phone = input("Phone:")
        email = input("Email:")
        data["people"].append({"name":name,"phone":phone,"email":email})
        with open('new_data','w') as json_file:
            json.dump(data,json_file,indent=2)
        print("New contact added")
        print('\n')
    elif n == 's':
        keyw = input('Please, enter search keywords:')
        l = search(keyw)
        print("Found",len(l),'entries:')
        for i in l:
            print('|' + str(i["NN"]) + ' |' + i["name"] + ' |' + i["phone"] + ' |' + i["email"])
            print('-' * 100)
    elif n == 'e':
        name = input('Please, enter contact name:')
        for pl in data['people']:
            if pl['name'] == name:
                print("""What field whould you like to change:
n - Name
p - Phone
e - Email""")
                s = input()
                if s == 'n':
                    new_n = input('Name:')
                    pl['name'] = new_n
                    with open('new_data','w') as json_file:
                        json.dump(data,json_file,indent=2)
                elif s == 'p':
                    new_p = input('Phone:')
                    pl['phone'] = new_p
                    with open('new_data','w') as json_file:
                        json.dump(data,json_file,indent=2)
                elif s == 'e':
                    new_e = input('Email:')
                    pl['email'] = new_e
                    with open('new_data','w') as json_file:
                        json.dump(data,json_file,indent=2)
    elif n == 'r':
        keyw = input('Please, enter search keywords:')
        l = search(keyw)
        print("Found",len(l),'entries:')
        for i in l:
           print('|' + str(i["NN"]) + ' |' + i["name"] + ' |' + i["phone"] + ' |' + i["email"])
           print('-' * 100)
        s = int(input('Please enter NN to delete:'))
        for pl in data['people']:
            if pl['name'] == l[s - 1]['name'] and pl['phone'] == l[s - 1]['phone'] and pl['email'] == l[s - 1]['email']:
                data['people'].remove(pl)
                with open('new_data','w') as json_file:
                       json.dump(data,json_file,indent=2)
                       break
