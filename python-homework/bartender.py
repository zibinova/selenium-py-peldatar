#ennel krealok egy meg jobbat, ez egy kicsit fapadosnak tűnik

x = input("Hány éves?")
y = input("Mit iszik?")

if int(x) < 18:
    if y == "sört":
       print("Nem kap")
    elif y == "kólát":
        print("Parancsoljon a kólája!")
    else:
        print("Csak sör és kóla van!")
if int(x) >= 60:
    if y == "sört":
        print("Parancsoljon a söre!")
    elif y == "kólát":
        print("A koffein megemelheti a vérnyomását!")
    else:
        print("Csak sör és kóla van!")
elif 18 <= int(x) < 60:
    if y == "sört":
        print("Parancsoljon a söre!")

    elif y == "kólát":
        print("Parancsoljon a kólája!")
    else:
        print("Csak sör és kóla van!")




