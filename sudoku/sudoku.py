# Feladat 1.
filename = input("Adja meg a bemeneti fájl nevét! ")
# filename = "konnyu.txt"
sor = int(input("Adja meg egy sor számát! "))
oszlop = int(input("Adja meg egy oszlop számát! "))


# Feladat 2.
sudoku = []
lepesek = []

with open(
    "C:\\Users\\User\\Documents\\Coding-Projects\\erettsegi-feladatok\\sudoku\\"
    + filename,
    "r",
) as file:
    for i in range(9):
        line = file.readline().strip().split(" ")
        digits = list(map(int, line))
        sudoku.append(digits)

    for line in file:
        digits = list(map(int, line.strip().split(" ")))
        lepesek.append(digits)


# Feladat 3.

ertek = sudoku[sor - 1][oszlop - 1]
if ertek == 0:
    print("Az adott helyet még nem töltötték ki.")
else:
    print(f"Az adott helyen szereplő szám: {ertek}")


def resztablazat(sor, oszlop):
    x = (oszlop - 1) // 3
    y = (sor - 1) // 3
    resz = x + y * 3 + 1
    return resz


print(f"A hely a(z) {resztablazat(sor, oszlop)} résztáblázathoz tartozik.")

# Feladat 4.
kitoltetlenek_szama = 0

for sor in range(9):
    for oszlop in range(9):
        ertek = sudoku[sor][oszlop]
        kitoltott = ertek != 0
        if not kitoltott:
            kitoltetlenek_szama += 1

szazalek = 100 * kitoltetlenek_szama / 81

print(f"Az üres helyek aránya: {round(szazalek, 2)}%")

# Feladat 5.

for lepes in lepesek:
    szam, sor, oszlop = lepes
    print(f"A kiválasztott sor: {sor} oszlop: {oszlop} a szám: {szam}")

    ertek = sudoku[sor - 1][oszlop - 1]
    if ertek != 0:
        print("A helyet már kitöltötték")
        continue

    # Sor
    szamok_a_sorban = sudoku[sor - 1]
    if szam in szamok_a_sorban:
        print("Az adott sorban már szerepel a szám")
        continue

    # Oszlop
    letezik_mar = False
    for i in range(9):
        if szam == sudoku[i][oszlop - 1]:
            letezik_mar = True

    if letezik_mar:
        print("Az adott oszlopban már szerepel a szám")
        continue

    # Resztablazat
    resz = resztablazat(sor, oszlop)
    resz_sor = ((resz - 1) // 3) * 3
    resz_oszlop = ((resz - 1) % 3) * 3

    letezik_mar = False

    for y in range(resz_sor, resz_sor + 3):
        for x in range(resz_oszlop, resz_oszlop + 3):
            if szam == sudoku[y][x]:
                letezik_mar = True

    if letezik_mar:
        print("Az adott résztáblázatban már szerepel a szám")
        continue

    print("A lépés megtehető")
