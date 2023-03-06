melysegek = []

# Feladat 1.

with open(
    "C:\\Users\\User\\Documents\\Coding-Projects\\erettsegi-feladatok\\godrok\\melyseg.txt"
) as file:
    for line in file:
        melysegek.append(int(line.strip()))

print(f"1. feladat\nA fájl adatainak száma: {len(melysegek)}")

# Feladat 2.

tavolsag = int(input("2. Feladat\nAdjon meg egy távolságértéket! ")) - 1
print(f"Ezen a helyen a felszín {melysegek[tavolsag]} méter mélyen van.")

# Feladat 3.

erintetlenek_szama = 0
for melyseg in melysegek:
    if melyseg == 0:
        erintetlenek_szama += 1

szazalek = erintetlenek_szama / len(melysegek) * 100

print(f"3. Feladat\nAz érintetlen terület aránya {round(szazalek, 2)}%")

# Feladat 4.

godrok = []

i = 0
elozo = 0
godor = []
for melyseg in melysegek:
    if melyseg != 0:
        godor.append(melyseg)
    elif elozo != 0:
        godrok.append(godor)
        godor = []

    elozo = melyseg


# Szamold ki hogy hanyadik godor
# megadott_tav_a_godorben = False
# for i in range(len(melysegek)):
#     melyseg = melysegek[i]
#     if i == tavolsag:
#         megadott_tav_a_godorben = True

#     if melyseg != 0:
#         godor.append(melyseg)
#     elif elozo != 0:
#         godrok.append(godor)
#         if megadott_tav_a_godorben:
#             print(f"A megadott érték a(z) {len(godrok)} gödörben van.")
#         megadott_tav_a_godorben = False
#         godor = []

#     elozo = melyseg


with open("./godrok.txt", "w") as file:
    file.write("")

    for godor in godrok:
        godor_de_str = map(str, godor)
        print(" ".join(godor_de_str), file=file)


# Feladat 5.
print(f"5. Feladat\nA gödrök száma: {len(godrok)}")

# Feladat 6.
print("6. Feladat")

if melysegek[tavolsag] == 0:
    print("Az adott helyen nincs gödör.")
else:
    # a
    kezdopont = tavolsag
    while melysegek[kezdopont - 1] != 0:
        kezdopont -= 1

    vegpont = tavolsag
    while melysegek[vegpont + 1] != 0:
        vegpont += 1

    print(
        f"a)\nA gödör kezdete: {kezdopont + 1} méter, a gödör vége: {vegpont + 1} méter."
    )

    # b
    print("b)")

    legmelyebb_ertek = 0
    legmelyebb_index = kezdopont

    for i in range(kezdopont, vegpont + 1):
        melyseg = melysegek[i]
        if melyseg > legmelyebb_ertek:
            legmelyebb_ertek = melyseg
            legmelyebb_index = i

    monoton = True

    # balrol
    for i in range(kezdopont, legmelyebb_index + 1):
        melyseg = melysegek[i]
        elozo_melyseg = melysegek[i - 1]
        if melyseg < elozo_melyseg:
            monoton = False

    # jobbrol
    for i in range(vegpont, legmelyebb_index - 1, -1):
        melyseg = melysegek[i]
        elozo_melyseg = melysegek[i + 1]
        if melyseg < elozo_melyseg:
            monoton = False

    if monoton:
        print("Folyamatosan mélyül.")
    else:
        print("Nem mélyül folyamatosan.")

    # c
    print(f"c)\nA legnagyobb mélysége {legmelyebb_ertek} méter.")

    # d
    terfogat = 0
    for i in range(kezdopont, vegpont + 1):
        melyseg = melysegek[i]
        terfogat += melyseg

    print(f"d)\nA térfogata {terfogat * 10} m^3.")

    # e
    vizmennyiseg = terfogat - (vegpont - kezdopont + 1)
    print(f"e)\nA vízmennyiség {vizmennyiseg * 10} m^3.")
