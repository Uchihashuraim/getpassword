import readchar 

def getpass():
    password = ""
    while True:
        char = readchar.readchar()
        if char == '\r':
            break
        elif char == '\b':
            password = password[:-1]
            print('\b \b', end='', flush=True)
        else:
            password += char
            print('*', end='', flush=True)
    return password

if __name__ == "__main__":
    print("Enter your password: ", end='', flush=True)
    password = getpass()
    print("\nYour password is:", password)