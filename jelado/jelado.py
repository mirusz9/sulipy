import math

jelek = []

with open(
    "C:\\Users\\User\\Documents\\Coding-Projects\\erettsegi-feladatok\\jelado\\jel.txt",
    "r",
) as file:
    for line in file:
        jel = line.strip().split()
        if len(jel) == 0:
            continue
        jelek.append(list(map(int, jel)))


# Feladat 2
sorszam = int(input("Add meg a jel sorszamat: "))
jel = jelek[sorszam - 1]
x = jel[3]
y = jel[4]
print("X: " + str(x) + ", Y: " + str(y))


# Feladat 3
def ido_masodpercben(ido):
    ora, perc, mperc = ido
    return mperc + perc * 60 + ora * 3600


def eltelt(ido1, ido2):
    mperc1 = ido_masodpercben(ido1)
    mperc2 = ido_masodpercben(ido2)

    eltelt_mperc = mperc2 - mperc1

    mperc = eltelt_mperc % 60
    perc = (eltelt_mperc // 60) % 60
    ora = eltelt_mperc // 3600

    return (ora, perc, mperc)


# Feladat 4

elso_jel = jelek[0]
utolso_jel = jelek[-1]
eltelt_ido = eltelt(elso_jel[0:3], utolso_jel[0:3])
ora, perc, mperc = eltelt_ido

print(f"{ora}:{perc}:{mperc}")


# Feladat 5

minx = 99999
miny = 99999
maxx = -99999
maxy = -99999

for jel in jelek:
    x = jel[3]
    y = jel[4]

    minx = min(minx, x)
    miny = min(miny, y)
    maxx = max(maxx, x)
    maxy = max(maxy, y)

print(
    f"A teglalap koordinatainak bal also es jobb felso sarka: ({minx}, {miny}) ({maxx}, {maxy})"
)


# Feladat 6

tavolsag = 0

for i in range(len(jelek) - 1):
    jel1 = jelek[i]
    jel2 = jelek[i + 1]

    dx = jel1[3] - jel2[3]
    dy = jel1[4] - jel2[4]

    tavolsag += math.sqrt(dx * dx + dy * dy)

print(f"Elmozdulas: {round(tavolsag, 3)} egyseg")


# Feladat 7

with open("kimaradt.txt", "w") as file:
    for i in range(len(jelek) - 1):
        jel1 = jelek[i]
        jel2 = jelek[i + 1]

        eltelt_ido = eltelt(jel1[0:3], jel2[0:3])
        ora, perc, mperc = eltelt_ido
        eltelt_ido_mperc = mperc + perc * 60 + ora * 3600

        kimaradt_jelek_szama_ido = (eltelt_ido_mperc - 1) // 300  # 300 mperc az 5 perc

        dx = abs(jel1[3] - jel2[3])
        dy = abs(jel1[4] - jel2[4])

        kimaradt_jelek_szama_tavolsag = (max(dx, dy) - 1) // 10

        if kimaradt_jelek_szama_ido > 0 or kimaradt_jelek_szama_tavolsag > 0:
            if kimaradt_jelek_szama_ido > kimaradt_jelek_szama_tavolsag:
                print(
                    f"{jel2[0]} {jel2[1]} {jel2[2]} idoelteres {kimaradt_jelek_szama_ido}",
                    file=file,
                )
            else:
                print(
                    f"{jel2[0]} {jel2[1]} {jel2[2]} koordinata-elteres {kimaradt_jelek_szama_tavolsag}",
                    file=file,
                )
