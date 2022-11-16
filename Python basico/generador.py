import random

def generate_password():

    mayus = ['A', 'B', 'C', 'D', 'E', 'F','G', 'H', 'I', 'J', 'K', 'L', 'M', 'N','Ñ', '0', 'P', 'Q', 'R', 'S', 'T', 'U','V', 'X', 'Y', 'Z']

    minus = ['a', 'b', 'c', 'd', 'e', 'f','g', 'h', 'i', 'j', 'k', 'l', 'm', 'ñ', 'o', 'p', 'q', 'r', 's', 't' 'u','v', 'x', 'y', 'z']

    nums = ['1', '2', '3', '4', '5', '6','7', '8', '9', '0']

    chars = ['**','*', '+', '-', '/', '@', '_', '?', '!', '[', '{', '(', ')', '}', ']','&', '$', '#', ']', ')', '}', 'l' ,'=' ]

    caracteres = mayus + minus + nums + chars

    password = []

    for i in range (50):
        c_random = random.choice(caracteres)
        password.append(c_random)

    password = "".join(password)
    return password

def run():
    password = generate_password()
    print("Tu nueva contraseña es: " + password)


if __name__ == '__main__':
    run()