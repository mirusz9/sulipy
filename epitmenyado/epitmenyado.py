telkek = []
savok = [100, 600, 800]
savIndex = {"A": 0, "B": 1, "C": 2}


# Feladat 1.
with open(
    "C:\\Users\\User\\Documents\\Coding-Projects\\erettsegi-feladatok\\epitmenyado\\utca.txt",
    "r",
) as file:
    lines = list(file)
    savokString = lines.pop(0).strip().split()
    for sav in savokString:
        savok.append(int(sav))

    for telek in lines:
        telkek.append(telek.strip().split())


# Feladat 2.
print(f"2. feladat. A mintában {len(telkek)} telek szerepel.")

# Feladat 3.
adoszam = input("3. Feladat. Egy tulajdonos adószáma: ")


def adoszam_filter(telek):
    return telek[0] == adoszam


tulajdonos_telkei = list(filter(adoszam_filter, telkek))

if len(tulajdonos_telkei) == 0:
    print("Nem szerepel az adatállományban.")
else:
    for telek in tulajdonos_telkei:
        print(f"{telek[1]} utca {telek[2]}")

# Feladat 4.
def ado(adosav, terulet):
    adosav_ar = savok[savIndex[adosav]]
    ado = adosav_ar * terulet

    if ado < 10000:
        return 0
    else:
        return ado


# Feladat .5
print("5. Feladat")


def adosav_filter_A(telek):
    return telek[3] == "A"


telkek_A = list(filter(adosav_filter_A, telkek))
ado_A = 0
for telek in telkek_A:
    ado_A += ado("A", int(telek[4]))

print(f"A sávba {len(telkek_A)} telek esik, az adó {ado_A} Ft.")


def adosav_filter_B(telek):
    return telek[3] == "B"


telkek_B = list(filter(adosav_filter_B, telkek))
ado_B = 0
for telek in telkek_B:
    ado_B += ado("B", int(telek[4]))

print(f"B sávba {len(telkek_B)} telek esik, az adó {ado_B} Ft.")


def adosav_filter_C(telek):
    return telek[3] == "C"


telkek_C = list(filter(adosav_filter_C, telkek))
ado_C = 0
for telek in telkek_C:
    ado_C += ado("C", int(telek[4]))

print(f"C sávba {len(telkek_C)} telek esik, az adó {ado_C} Ft.")

# Feladat 6.

utcak = {}

for telek in telkek:
    utcanev = telek[1]
    if utcanev not in utcak:
        utcak[utcanev] = [telek]
    else:
        utcak[utcanev].append(telek)


print("6. Feladat. A több sávba sorolt utcák:")

for utca in utcak:
    telkekazutcaban = utcak[utca]

    adosavok = []

    for telek in telkekazutcaban:
        adosav = telek[3]
        if adosav not in adosavok:
            adosavok.append(adosav)

    if len(adosavok) > 1:
        print(utca)

# Feladat 7.

with open("fizetendo.txt", "w") as file:
    file.write("")

    tulajdonosok = {}

    for telek in telkek:
        tulajdonos_adoszama = telek[0]
        if tulajdonos_adoszama not in tulajdonosok:
            tulajdonosok[tulajdonos_adoszama] = [telek]
        else:
            tulajdonosok[tulajdonos_adoszama].append(telek)

    for tulaj in tulajdonosok:
        tulaj_telkei = tulajdonosok[tulaj]

        fizetendo = 0

        for telek in tulaj_telkei:
            terulet = int(telek[4])
            adosav = telek[3]
            fizetendo += ado(adosav, terulet)

        print(f"{tulaj} {fizetendo}", file=file)
