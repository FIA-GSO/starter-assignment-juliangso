from tabulate import tabulate


# TODO create table


def run():
    print("Flächeninhalt: ")
    flaecheninhalt = int(input())
    a = flaecheninhalt
    b = 1
    abweichung = a - b

    while abweichung > 0.01:
        a = calc_mittelwert(a, b)
        b = flaecheninhalt / a
        abweichung = a - b

        print(f"a: {a}")
        print(f"b: {b}")
        print(f"abweichung: {abweichung}")


def calc_mittelwert(a, b):
    return (a+b)/2

