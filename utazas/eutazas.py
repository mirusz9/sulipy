# Feladat 1

beolvasasok = []

with open(
    "C:\\Users\\User\\Documents\\Coding-Projects\\erettsegi-feladatok\\utazas\\utasadat.txt",
    "r",
) as file:
    for line in file:
        megallo, datumesido, azonosito, tipus, ervenyesseg = line.strip().split(" ")
        datum, ido = datumesido.split("-")
        beolvasasok.append(
            {
                "megallo": int(megallo),
                "datum": datum,
                "ido": ido,
                "azonosito": azonosito,
                "tipus": tipus,
                "ervenyesseg": ervenyesseg,
            }
        )

# Feladat 2.
print(f"2. feladat\nA buszra {len(beolvasasok)} utas akart felszállni.")

# Feladat 3.
elutasitottak_szama = 0

for felszallas in beolvasasok:
    if felszallas["tipus"] == "JGY":
        if felszallas["ervenyesseg"] == "0":
            elutasitottak_szama += 1
    else:
        if felszallas["datum"] > felszallas["ervenyesseg"]:
            elutasitottak_szama += 1

print(f"3. feladat\nA buszra {elutasitottak_szama} utas nem szállhatott fel.")

# Feladat 4.

megallokkent = {}

for beolvasas in beolvasasok:
    if beolvasas["megallo"] not in megallokkent:
        megallokkent[beolvasas["megallo"]] = 1
    else:
        megallokkent[beolvasas["megallo"]] += 1

legtobb_ember_szama = 0
keresettmegallo = 0

for megallo in megallokkent:
    felszallo_emberek = megallokkent[megallo]
    if felszallo_emberek > legtobb_ember_szama:
        legtobb_ember_szama = felszallo_emberek
        keresettmegallo = megallo

print(
    f"4. feladat\nA legtöbb utas ({legtobb_ember_szama} fő) a {keresettmegallo}. megállóban próbált felszállni."
)

# Feladat 5.
kedvezmenyes = 0
ingyenes = 0

for felszallas in beolvasasok:
    tipus = felszallas["tipus"]
    if tipus != "JGY" and felszallas["datum"] <= felszallas["ervenyesseg"]:
        if tipus == "TAB" or tipus == "NYB":
            kedvezmenyes += 1
        elif tipus == "NYP" or tipus == "RVS" or tipus == "GYK":
            ingyenes += 1

print(
    f"5. feladat\nIngyenesen utazók száma: {ingyenes} fő\nA kedvezményesen utazók száma: {kedvezmenyes} fő"
)

# Feladat 6.


def napokszama(e1, h1, n1, e2, h2, n2):
    h1 = (h1 + 9) % 12
    e1 = e1 - h1 // 10
    d1 = 365 * e1 + e1 // 4 - e1 // 100 + e1 // 400 + (h1 * 306 + 5) // 10 + n1 - 1
    h2 = (h2 + 9) % 12
    e2 = e2 - h2 // 10
    d2 = 365 * e2 + e2 // 4 - e2 // 100 + e2 // 400 + (h2 * 306 + 5) // 10 + n2 - 1

    return d2 - d1


# Feladat 7.

with open("figyelmeztetes.txt", "w") as file:
    for beolvasas in beolvasasok:
        if beolvasas["tipus"] == "JGY":
            continue

        datum = beolvasas["datum"]
        e1 = int(datum[0:4])
        h1 = int(datum[4:6])
        n1 = int(datum[6:8])

        erv = beolvasas["ervenyesseg"]
        e2 = int(erv[0:4])
        h2 = int(erv[4:6])
        n2 = int(erv[6:8])

        kulonbseg = napokszama(e1, h1, n1, e2, h2, n2)
        if kulonbseg > 0 and kulonbseg <= 3:
            azonosito = beolvasas["azonosito"]
            print(f"{azonosito} {e2}-{h2}-{n2}", file=file)
