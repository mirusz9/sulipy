lista = [1, 2, 3, 4, 5, 6]

def duplazo(szam):
    return szam * 2

lista2 = list(map(duplazo, lista))

stringek = ["1", "2", "3", "4"]

stringek2 = list(map(int, stringek))

print(lista2)
print(stringek2)