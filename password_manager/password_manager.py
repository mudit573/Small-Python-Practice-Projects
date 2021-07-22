
from cryptography.fernet import Fernet

def load_key():
    file =  open("E:\Projects\Small_Python_Projects\password_manager\key.key","rb")
    key = file.read()
    file.close()
    return key

'''
def write_key():
    key = Fernet.generate_key()
    with open("E:\Projects\Small_Python_Projects\password_manager\key.key","wb") as key_file:
        key_file.write(key)'''

key  = load_key()
fer = Fernet(key)

def view():
    with open('E:\Projects\Small_Python_Projects\password_manager\password.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user,passw = data.split("|")
            print("User:",user,"| password:",
                    fer.decrypt(passw.encode()).decode())



def add():
    name = input("Account Name: ")
    pwd = input("Password: ")

    with open('E:\Projects\Small_Python_Projects\password_manager\password.txt', 'a') as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + " \n")




while True:
    mode = input("Would you like to adda new passwod or view existing ones(view, add), press q to quit: ").lower()
    if mode == "q":
        break
    
    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode. ")
        continue