def run():
    # Squares = []
    # for i in range(1, 101):
    #     if i % 3 != 0:
    #         Squares.append(i**2)

    # Squares = [i **2 for i in range(1, 101) if i % 3 != 0]

    Squares = [i for i in range(1, 10001) if i % 36 == 0]

    print(Squares)


if __name__ == '__main__':
    run()