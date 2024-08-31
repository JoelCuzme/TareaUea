lista=[
    [4,2,3],
    [1,0,5],
    [9,8,7]
]
print("Matriz original")
for matriz in lista:
    print(matriz)


def imprimir(lista):
    for matriz in lista:
        print (matriz)

def primero(lista):
    a = len(lista)
    for i in range(a):
        for j in range(0, a-i-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]


def ordenar_fila(lista,fil):
    primero(lista[fil])

    print(f"Matriz con la fila {fil} ordenada:")
    imprimir(lista)

fil = 1

ordenar_fila(lista, fil)