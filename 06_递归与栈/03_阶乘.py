def fact(x):
    if x == 1:
        return x
    return x * fact(x - 1)


def fact2(x):
    return 1 if x == 0 else x * fact2(x - 1)


if __name__ == '__main__':
    # print(fact(5))
    print(fact2(5))
