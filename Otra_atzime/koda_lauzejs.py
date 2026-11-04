apaksa = 1
augsa = 100
gājieni = 0

while True:
    minejums = (apaksa + augsa) // 2
    print(f"Mans minējums ir {minejums}.")
    gājieni += 1
    atbilde = input("Vai tas ir tavs skaitlis? Vai tas ir Lielāks/Mazāks/Pareizs? L/M/P:")

    if atbilde == "P":
        print(f"Es uzminēju tavu skaitli {gājieni} gājienos!")
        break
    if atbilde == "L":
        apaksa = minejums + 1
        minejums = (apaksa + augsa) // 2
    if atbilde == "M":
        augsa = minejums - 1
        minejums = (apaksa + augsa) // 2
    else:
        print("Tā nav opcija!")
    
    if apaksa > augsa:
        print("Tavi apgalvojumi nesakrīt! Ja negribi sadarboties, es beidzu spēli!")
        break

# pirmā partija - 43. 4 gājieni
# otrā partija - 99. 6 gājieni
# trešā partija - 2. 7 gājieni
# Lielākais gājienu skaits ir 7.
# Lineārajai stratēģijai sliktākā gadījumā vajadzētu 100 gājienus, 
# jo, ja skaitlis ir 100, tad dators ies cauri visiem iepriekšējiem skaitļiem.
