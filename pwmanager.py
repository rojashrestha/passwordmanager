import os
from cryptography.fernet import Fernet #this allows you to encrypt text (convert (information or data) into a code, especially to prevent unauthorized access.)


def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    with open("key.key", "rb") as file:
        key = file.read()
    return key

if not os.path.exists("key.key"):
    print("Encryption key not found. Generating a new one...")
    write_key()

key = load_key()
fer = Fernet(key)

def view():
    if not os.path.exists('password.txt'):
        print("No passwords saved yet!")
        return

    with open('password.txt', 'r') as f:
        for line in f.readlines():
            data = (line.rstrip())
            user, passw = data.split("|")
            print("User:", user, ", Password:", fer.decrypt(passw.encode()).decode())

def add():
    name = input('Account name: ')
    pw = input('Password: ')
    with open('password.txt', 'a') as f:
        f.write(name + "|" + fer.encrypt(pw.encode()).decode() + "\n")

while True:
    mode = input("Would you like to add a new password or view the existing ones (view, add)? Press 'q' to quit: ").lower()

    if mode == "q":
        break
    elif mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode. Please enter 'view', 'add', or 'q'.")
