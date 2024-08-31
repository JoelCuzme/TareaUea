lista=[
    [4,2,3],
    [1,0,5],
    [9,8,7]
]
buscar=int(input("Coloque el numero que busca:"))

fencontrada= -2
cencontrada= -2

for fila in range(len(lista)):
    for columna in range (len(lista[fila])):
        if lista[fila][columna] == buscar:
            fencontrada= fila
            cencontrada= columna
            break
    if fencontrada != -2:
        break
if fencontrada != -2:
    print("Se encontro",buscar,"en la fila",fencontrada,"y columna",cencontrada)
else:
    print("Dato no existente en lista")