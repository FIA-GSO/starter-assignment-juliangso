def run():
    print("Geben sie ihre Messwerte einzeln ab. Wenn sie fertig sind, beenden sie mit (Q/q)")
    messwerte = []
    while True:
        user_input = input()
        try:
            messwerte.append(int(user_input))
        except ValueError:
            if user_input == 'q' or user_input == 'Q':
                output(messwerte)
                return


def output(messwerte):
    print(messwerte)
    print(f"max {find_max(messwerte)}")
    print(f"min {find_min(messwerte)}")


def find_max(messwerte):
    maximum = messwerte[0]
    for i in messwerte:
        if i > maximum:
            maximum = i
    return maximum


def find_min(messwerte):
    minimum = messwerte[0]
    for i in messwerte:
        if i < minimum:
            minimum = i
    return minimum
