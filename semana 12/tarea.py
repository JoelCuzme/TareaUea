#3x4x7
matriz= \
[
    [
        [20,15,18,20,14,15,19],
        [24,25,24,26,21,20,21],
        [20,21,19,19,18,19,20],
        [27,24,25,21,20,21,21]
    ],
    [
        [22,25,24,21,21,21,20],
        [25,20,20,21,23,23,27],
        [18,14,15,14,17,18,14],
        [16,14,15,17,18,17,14]
    ],
    [
        [18,17,19,15,17,15,17],
        [18,19,18,18,17,18,18],
        [20,25,14,17,18,15,17],
        [25,24,20,25,24,20,21]
    ]
]

while True:
    ciudad = str(input("Ingrese el nombre de la ciudad que busca: "))
    if ciudad == "Puyo":
        ciudad = int (0)
        while True:
            semana = int((input("Ingrese el numero de la semana que desea: ")))
            if semana >= 5 or semana <= 0:
                print ("semana no encontrda")
            else:
                break
        semana_f = int(semana - 1)
        promedio=0
        for a in matriz[ciudad][semana_f]:
            promedio += a
            tem_promedio = promedio/7
            tem_promedio = round(tem_promedio,2)
        print(f"La temperatura promedio de la semana {semana} es de {tem_promedio}°C")

    elif ciudad =="Ambato":
        ciudad = int(1)
        while True:
            semana = int(input("Ingrese el numero de la semana que desea: "))
            if semana >= 5 or semana <= 0:
                print("semana no encontrda")
            else:
                break
        semana_f = int(semana - 1)
        promedio = 0
        for a in matriz[ciudad][semana_f]:
            promedio += a
            tem_promedio = promedio / 7
            tem_promedio = round(tem_promedio, 2)
        print(f"La temperatura promedio de la semana {semana} es de {tem_promedio}°C")

    elif ciudad == "Baños":
        ciudad = int(2)
        while True:
            semana = int(input("Ingrese el numero de la semana que desea: "))
            if semana >= 5 or semana <= 0:
                print("semana no encontrda")
            else:
                break
        semana_f = int(semana - 1)
        promedio = 0
        for a in matriz[ciudad][semana_f]:
            promedio += a
            tem_promedio = promedio / 7
            tem_promedio = round(tem_promedio, 2)
        print(f"La temperatura promedio de la semana {semana} es de {tem_promedio}°C")
    else:
        print("No encontrado")










