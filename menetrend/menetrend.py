# Feladat 1.

menetrend = {}

with open(
    "C:\\Users\\User\\Documents\\Coding-Projects\\erettsegi-feladatok\\menetrend\\vonat.txt"
) as file:
    for line in file:
        vonatAzonosito, allomasAzonosito, ora, perc, irany = line.strip().split("\t")

        if vonatAzonosito not in menetrend:
            menetrend[vonatAzonosito] = {
                allomasAzonosito: {
                    irany: {
                        "ora": int(ora),
                        "perc": int(perc),
                        "ido": int(ora) * 60 + int(perc),
                    }
                }
            }
        elif allomasAzonosito not in menetrend[vonatAzonosito]:
            menetrend[vonatAzonosito][allomasAzonosito] = {
                irany: {
                    "ora": int(ora),
                    "perc": int(perc),
                    "ido": int(ora) * 60 + int(perc),
                }
            }
        else:
            menetrend[vonatAzonosito][allomasAzonosito][irany] = {
                "ora": int(ora),
                "perc": int(perc),
                "ido": int(ora) * 60 + int(perc),
            }

# Feladat 2.
allomasok = len(menetrend["1"])
print(f"2. feladat\nAz állomások száma: {allomasok}\nA vonatok száma: {len(menetrend)}")

# Feladat 3.
leghosszabbIdo = 0
leghvonat = ""
leghallomas = ""

for vonat in menetrend:
    vonatMenetrendje = menetrend[vonat]
    for allomas in vonatMenetrendje:
        if "E" not in vonatMenetrendje[allomas] or "I" not in vonatMenetrendje[allomas]:
            continue

        erkezes = vonatMenetrendje[allomas]["E"]
        indulas = vonatMenetrendje[allomas]["I"]

        eltelt = indulas["ido"] - erkezes["ido"]

        if eltelt > leghosszabbIdo:
            leghosszabbIdo = eltelt
            leghvonat = vonat
            leghallomas = allomas

print(
    f"3. feladat\nA(z) {leghvonat}. vonat a(z) {leghallomas}. állomáson {leghosszabbIdo} percet állt."
)

# Feladat 4.

vonatAzonosito = input("4. feladat\nAdja meg egy vonat azonosítóját! ")
megadottOra, megadottPerc = input("Adjon meg egy időpontot (óra perc)! ").split(" ")

# Feladat 5.

eloirt = 2 * 60 + 22
indulas = menetrend[vonatAzonosito]["0"]["I"]
erkezes = menetrend[vonatAzonosito]["10"]["E"]

kulonbseg = erkezes["ido"] - indulas["ido"] - eloirt

if kulonbseg == 0:
    print(f"A(z) {vonatAzonosito}. vonat útja pontosan az előírt ideig tartott.")
elif kulonbseg > 0:
    print(
        f"A(z) {vonatAzonosito}. vonat útja {kulonbseg} perccel hosszabb volt az előírtnál."
    )
else:
    print(
        f"A(z) {vonatAzonosito}. vonat útja {-kulonbseg} perccel rövidebb volt az előírtnál."
    )


# Feladat 6.

with open(f"halad{vonatAzonosito}.txt", "w", encoding="utf-8") as file:
    for allomas in menetrend[vonatAzonosito]:
        if allomas == "0":
            continue
        erkezett = menetrend[vonatAzonosito][allomas]["E"]
        ora = erkezett["ora"]
        perc = erkezett["perc"]
        print(f"{allomas}. állomás: {ora}:{perc}", file=file)

# Feladat 7.
print("7. feladat")

megadottIdo = int(megadottOra) * 60 + int(megadottPerc)


for vonat in menetrend:
    for allomasIndex in range(len(menetrend[vonat]) - 1):
        allomas = menetrend[vonat][str(allomasIndex)]
        indulas = allomas["I"]["ido"]

        kovAllomas = menetrend[vonat][str(allomasIndex + 1)]
        kovErkezes = kovAllomas["E"]["ido"]

        if allomasIndex == 0:
            if indulas < megadottIdo and megadottIdo < kovErkezes:
                print(
                    f"A(z) {vonat}. vonat a {allomasIndex}. és a {allomasIndex + 1}. állomás között járt. "
                )
            continue

        erkezes = allomas["E"]["ido"]

        if erkezes <= megadottIdo and megadottIdo <= indulas:
            print(f"A(z) {vonat}. vonat a {allomasIndex}. állomáson állt.")
        if indulas < megadottIdo and megadottIdo < kovErkezes:
            print(
                f"A(z) {vonat}. vonat a {allomasIndex}. és a {allomasIndex + 1}. állomás között járt. "
            )
