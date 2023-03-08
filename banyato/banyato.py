sorok = 0
oszlopok = 0

melysegek = []

# Feladat 1.

with open(
    "C:\\Users\\User\\Documents\\Coding-Projects\\erettsegi-feladatok\\banyato\\melyseg.txt",
    "r",
) as file:
    sorok = int(file.readline().strip())
    oszlopok = int(file.readline().strip())

    for sor in file:
        int_sor = list(map(int, sor.strip().split(" ")))
        melysegek.append(int_sor)

# Feladat 2.

sor = int(input("2. Feladat\nA mérés sorának azonosítója="))
oszlop = int(input("A mérés oszlopának azonosítója="))

print(f"A mért mélység az adott helyen {melysegek[sor - 1][oszlop - 1]} dm")

# Feladat 3.

felszin = 0
osszmelyseg = 0

for sor in melysegek:
    for melyseg in sor:
        osszmelyseg += melyseg
        if melyseg != 0:
            felszin += 1

atlagmelyseg = osszmelyseg / (
    felszin * 10
)  # 10-zel osztas a dm-bol meterre atszamitas miatt

print(
    f"3. Feladat\nA tó felszíne: {felszin} m2, átlagos mélysége: {round(atlagmelyseg, 2)} m"
)

# Feladat 4.

legmelyebb = 0
legmelyebb_koordinatak = []

for sor in range(sorok):
    for oszlop in range(oszlopok):
        melyseg = melysegek[sor][oszlop]

        if melyseg == legmelyebb:
            legmelyebb_koordinatak.append([sor, oszlop])
        elif melyseg > legmelyebb:
            legmelyebb = melyseg
            legmelyebb_koordinatak = []
            legmelyebb_koordinatak.append([sor, oszlop])


print("4. Feladat\nA legmélyebb helyek sor-oszlop koordinátái:")
for koordinata in legmelyebb_koordinatak:
    sor = koordinata[0] + 1
    oszlop = koordinata[1] + 1
    print(f"({sor}; {oszlop})  ", end="")

# Feladat 5.

parthossz = 0

for sor in range(1, sorok - 1):
    for oszlop in range(1, oszlopok - 1):
        melyseg = melysegek[sor][oszlop]

        if melyseg != 0:  # Ha az adott hely a tohoz tartozik
            # Mind a 4 valtozo True vagy False attol fuggoen hogy a parthoz tartozik vagy nem
            fel = melysegek[sor - 1][oszlop] == 0
            le = melysegek[sor + 1][oszlop] == 0
            balra = melysegek[sor][oszlop - 1] == 0
            jobbra = melysegek[sor][oszlop + 1] == 0

            parthossz += int(fel) + int(le) + int(balra) + int(jobbra)

print(f"\n5. Feladat\nA tó partvonala {parthossz} m hosszú")

# Feladat 6.

oszlop = int(input("6. Feladat\nA vizsgált szelvény oszlopának azonosítója=")) - 1

with open("diagram.txt", "w") as file:
    file.write("")

    for sor in range(sorok):
        melyseg = melysegek[sor][oszlop]
        kerekitett = round(melyseg / 10)
        csillagok = "*" * kerekitett

        if sor + 1 < 10:
            print(f"0{sor + 1}{csillagok}", file=file)
        else:
            print(f"{sor + 1}{csillagok}", file=file)
