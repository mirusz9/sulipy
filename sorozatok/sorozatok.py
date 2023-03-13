# Feladat 1.

epizodok = []

with open(
    "C:\\Users\\User\\Documents\\Coding-Projects\\erettsegi-feladatok\\sorozatok\\lista.txt",
    "r",
) as file:
    file = list(file)
    sorok_szama = len(file)
    for i in range(int(sorok_szama / 5)):
        datum = file[5 * i].strip()
        nev = file[5 * i + 1].strip()
        evadesepizod = file[5 * i + 2].strip()
        epizod_hossz = file[5 * i + 3].strip()
        megnezte = file[5 * i + 4].strip()

        epizod = {
            "datum": datum,
            "nev": nev,
            "evadesepizod": evadesepizod,
            "epizod_hossz": int(epizod_hossz),
            "megnezte": int(megnezte),
        }

        epizodok.append(epizod)


# Feladat 2, 3, 4

szamlalo = 0
latta = 0
eltoltott_percek = 0

for epizod in epizodok:
    if epizod["datum"] != "NI":
        szamlalo += 1
    if epizod["megnezte"] == 1:
        latta += 1
        eltoltott_percek += epizod["epizod_hossz"]

print(f"2. Feladat\nA listában {szamlalo} db vetítési dátummal rendelkező epizód van.")

szazalek = 100 * latta / len(epizodok)

print(f"3. Feladat\nA listában lévő epizódok {round(szazalek, 2)}%-át látta.")

percek = eltoltott_percek % 60
orak = eltoltott_percek // 60 % 24
napok = eltoltott_percek // 60 // 24

print(
    f"4. Feladat\nSorozatnézéssel {napok} napot {orak} órát és {percek} percet töltött."
)

# Feladat 5.

datum = input("5. Feladat\nAdjon meg egy dátumot! Dátum= ")
evI, hoI, napI = datum.split(".")

napInput = 365 * int(evI) + 31 * int(hoI) + int(napI)


for epizod in epizodok:
    if epizod["datum"] == "NI":
        continue

    ev, ho, nap = epizod["datum"].split(".")
    epizodNap = 365 * int(ev) + 31 * int(ho) + int(nap)

    if epizod["megnezte"] == 0 and epizodNap <= napInput:
        evadesepizod = epizod["evadesepizod"]
        nev = epizod["nev"]
        print(f"{evadesepizod}\t{nev}")

# Feladat 6.


def hetnapja(ev, ho, nap):
    napok = ["v", "h", "k", "sze", "cs", "p", "szo"]
    honapok = [0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4]
    if ho < 3:
        ev -= 1

    hetnapja = napok[(ev + ev // 4 - ev // 100 + ev // 400 + honapok[ho - 1] + nap) % 7]

    return hetnapja


# Feladat 7.
megadott_napon_vetitett = set()

megadottNap = input("7. Feladat\nAdja meg a hét egy napját (például cs)! Nap= ")

for epizod in epizodok:
    if epizod["datum"] == "NI":
        continue
    ev, ho, nap = epizod["datum"].split(".")

    if megadottNap == hetnapja(int(ev), int(ho), int(nap)):
        megadott_napon_vetitett.add(epizod["nev"])

if len(megadott_napon_vetitett) == 0:
    print("Az adott napon nem kerül adásba sorozat.")
else:
    for epizod in megadott_napon_vetitett:
        print(epizod)


# Feladat 8.

sorozatonkent = {}

for epizod in epizodok:
    nev = epizod["nev"]
    if nev not in sorozatonkent:
        sorozatonkent[nev] = {"nev": nev, "hossz": epizod["epizod_hossz"], "epizodok_szama": 1}
    else:
        sorozatonkent[nev]["hossz"] += epizod["epizod_hossz"]
        sorozatonkent[nev]["epizodok_szama"] += 1


with open("summa.txt", "w") as file:
    for sorozat_nev in sorozatonkent:
        sorozat = sorozatonkent[sorozat_nev]
        nev = sorozat["nev"]
        hossz = sorozat["hossz"]
        epizodok_szama = sorozat["epizodok_szama"]
        print(f"{nev} {hossz} {epizodok_szama}", file=file)
