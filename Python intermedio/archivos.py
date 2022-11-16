from ast import With


def read ():
    numbers = []
    with open("./archivos/Numbers.txt", "r", encoding="utf-8") as f:
        for line in f:
            numbers.append(int(line))
    print(numbers)


def write ():
    names = ["andres", "bryan", "cossich", "dulce"]
    with open("./archivos/Names.txt", "a", encoding="utf-8") as f:
        for name in names:
            f.write(name)
            f.write("\n")


def run ():
    write ()




if __name__ == '__main__':
    run()