ev = int(input("Kérem az évet!"))


def szoko(evi):
    if ev % 4 == 0 and (ev % 100 != 0 or ev % 400 == 0):
        print("Szökőév")
    else:
        print("Nem szökőév")


szoko(ev)
