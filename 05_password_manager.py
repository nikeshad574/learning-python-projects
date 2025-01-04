from cryptography.fernet import Fernet

def load_key():
    try:
        with open("key.key", "r") as f:
            return f.readline().strip()
    
    except FileNotFoundError:
        with open("key.key", "w") as f:
                key = Fernet.generate_key()
                f.write(key.decode())
                return key.decode()
        

key = load_key()
fernet = Fernet(key)

print("------------------ Password Manager -------------------")

def addPassword():
    name = input("Name: ")
    password = input("Password: ")

    with open("pw.txt", "a") as f:
        f.write(f"{name}|{fernet.encrypt(password.encode()).decode()}\n")
        print("Your password was saved!")


def readPassword():
    try:
        with open("pw.txt", "r") as f:
            print("\n-- All Password --")
            for line in f.readlines():
                splitLine = line.strip().split("|")
                print(f"Name: {splitLine[0]} | Password: {fernet.decrypt(splitLine[1].encode()).decode()}")
    except FileNotFoundError:
        print("No Password Saved Yet!!!")


while True: 
    userChoice = input("\nWhat to do? 0 = add, 1 = see all, q = quit: ")

    if(userChoice == "q"):
        print("Thankyou for using!")
        quit()

    if (userChoice.isdigit()):
        userChoice = int(userChoice)
    else:
        print("Invalid!")
        continue

    if userChoice == 0:
        addPassword()
    elif userChoice == 1:
        readPassword()
    else:
        print("Invalid!")
        continue