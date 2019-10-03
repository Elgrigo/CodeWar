#from tabulate import tabulate
import argparse 
import time
import json
import os
import shutil
import sqlite3


parser = argparse.ArgumentParser()
parser.add_argument("--path",help="your name",default="C:/Users/Toshiba/Desktop/CodeWarriors/Problems/File Manager/My Files",type=str)
args = parser.parse_args()

conn = sqlite3.connect('File.db')
            
c = conn.cursor()

#c.execute("""CREATE TABLE files(
#                Name text,
#                Size integer,
#                ModDates text
#                )""")

def Json_dump():
    with open('Data_Table','w') as json_file:
        json.dump(data,json_file,indent=2)

def insert_file_dict(name,size,time):
    with conn:
            c.execute("INSERT INTO files VALUES(:Name,:Size,:ModDates)",
                        {"Name":name,"Size":size,"ModDates": time})

def delete_file_dict(name):
    with conn:
            c.execute("DELETE from files Where Name = :Name",
                        {"Name":name})

def update_name(O_name,N_name,time):
    with conn:
        c.execute("""UPDATE files SET Name = :New , ModDates=:ModDates
                        WHERE Name=:Old""",
                        {'New':N_name,'Old':O_name,'ModDates':time})

def update_size(name,size,time):
    with conn:
        c.execute("""UPDATE files SET Size = :Size , ModDates=:ModDates WHERE Name=:Name""",
                        {'Name':name,'Size':size,'ModDates':time})

while True:
    print("""Your comands are:
ls <path> - list directory content with the file sizes, creation and modification dates
cf <filename> - creates a file with given name
cd <dirname> - creates a directory with given name
df <filename> - deletes a file with given name
dd <dirname> - deletes a directory with given name
m <old/path> <new/path> - moves/renames a file from old to new
i <filename> <mode> <any text> - append (mode == 'a') or write/truncate (mode == 'w') any given text into the file
s <filename> - shows content of the file
q - exists from the program
""")
    cmd = input("cmd>>")

    if cmd == "ls":
        c.execute("SELECT * FROM files")
        print(c.fetchall())

    elif cmd == "cf":
        name = input("File name:")
        filepath = os.path.join(args.path,name)
        open(filepath,"a").close()
        time1 = time.asctime()
        insert_file_dict(name,os.path.getsize(args.path + "/" + name),str(time1))

    elif cmd == "cd":
        name = input("Directory name:")
        filepath = os.mkdir(args.path + "/" + name)
        time1 = time.asctime()
        insert_file_dict(name,os.path.getsize(args.path + "/" + name),str(time1))

    elif cmd == "df":
        name = input("File name:")
        os.remove(args.path + "/" + name)
        delete_file_dict(name)  

    elif cmd == "dd":
       name = input("Directory name:")
       os.rmdir(args.path + "/" + name)
       delete_file_dict(name)

    elif cmd == "m":
        old_name = input("Old Name:")
        new_name = input("New Name:")
        old_path = input("Old Path:")
        new_path = input("New Path:")
        shutil.move(old_path + '/' + old_name,new_path + '/' + new_name)
        time1 = time.asctime()
        update_name(old_name,new_name,str(time1))

    elif cmd == "i":
        name = input("File name:")
        mode = input("Enret mode:")
        text = input("Your text:")
        filepath = os.path.join(args.path,name)
        if mode == "w":
            file = open(filepath,"w+")
        else:
            file = open(filepath,"a+")
        file.write(text)
        file.close()
        time1 = time.asctime()
        size = os.path.getsize(args.path + "/" + name)
        update_size(name,size,str(time1))

    elif cmd == "s":
        name = input("File name:")
        filepath = os.path.join(args.path,name)
        f = open(filepath,"r")
        content = f.read()
        print(content)
        print("\n")

    elif cmd == "q":
        print("Bye :)")
        break
