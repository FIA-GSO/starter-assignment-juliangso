from tabulate import tabulate


menge_list = []


def run():
    add_data(10, 10, 10)

    i = 0
    while i < 10:
        jung = calc_jung(menge_list[i].get("Erw"), menge_list[i].get("Alt"))
        erw = calc_erwachsen(menge_list[i].get("Jung"))
        alt = calc_alt(menge_list[i].get("Erw"))
        add_data(jung, erw, alt)
        i += 1
    print_output()


def add_data(jung, erw, alt):
    menge_list.append({"Jung": jung, "Erw": erw, "Alt": alt})


def print_output():
    headers = menge_list[0].keys()
    rows = []
    for x in menge_list:
        rows.append(x.values())

    table = tabulate(rows, headers, tablefmt="github")
    print(table)


def calc_jung(erwachsen, alt):
    return int(erwachsen*4 + alt*2)


def calc_erwachsen(jung):
    return int(jung/2)


def calc_alt(erwachsen):
    return int(erwachsen/3)
