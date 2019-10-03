import json
with open('new_data','r') as json_file:
    data = json.load(json_file)

def print_search():
    for i in people_list:
        print('|' + str(i["NN"]) + ' |' + i["name"] + ' |' + i["phone"] + ' |' + i["email"])
        print('-' * 100)

def search(s):
    k = 0
    people_list = list()
    for person in data["persons"]:
        if person['name'].count(s) > 0 or person['phone'].count(s) > 0 or person['email'].count(s) > 0:
            k+=1
            people_list.append({"NN":k,"name":person['name'],"phone":person['phone'],"email":person['email']})
    return people_list

def Json_dump():
    with open('new_data','w') as json_file:
        json.dump(data,json_file,indent=2)

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
        data["persons"].append({"name":name,"phone":phone,"email":email})
        Json_dump()
        print("New contact added")
        print('\n')
    elif n == 's':
        keyword = input('Please, enter search keywords:')
        people_list = search(keyword)
        print("Found",len(people_list),'entries:')
        print_search()
    elif n == 'e':
        name = input('Please, enter contact name:')
        for person in data["persons"]:
            if person['name'] == name:
                print("""What field whould you like to change:
n - Name
p - Phone
e - Email""")
                s = input()
                if s == 'n':
                    new_n = input('Name:')
                    person['name'] = new_n
                    Json_dump()
                elif s == 'p':
                    new_p = input('Phone:')
                    person['phone'] = new_p
                    Json_dump()
                elif s == 'e':
                    new_e = input('Email:')
                    person['email'] = new_e
                    Json_dump()
    elif n == 'r':
        keyword = input('Please, enter search keywords:')
        people_list = search(keyword)
        print("Found",len(people_list),'entries:')
        print_search()
        s = int(input('Please enter NN to delete:'))
        for person in data['persons']:
            if person['name'] == l[s - 1]['name'] and person['phone'] == l[s - 1]['phone'] and person['email'] == l[s - 1]['email']:
                data['persons'].remove(person)
                Json_dump()
                break
