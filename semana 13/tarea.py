#se definieron diccionares para poder manipular los datos de mejor manera
Puyo={
    "semana 1":[20,15,18,20,14,15,19],
    "semana 2":[24,25,24,26,21,20,21],
    "semana 3":[20,21,19,19,18,19,20],
    "semana 4":[27,24,25,21,20,21,21]
    }
Baños={
    "semana 1":[22,25,24,21,21,21,20],
    "semana 2":[25,20,20,21,23,23,27],
    "semana 3":[18,14,15,14,17,18,14],
    "semana 4":[16,14,15,17,18,17,14]
    }
Ambato={
    "semana 1":[18,17,19,15,17,15,17],
    "semana 2":[18,19,18,18,17,18,18],
    "semana 3":[20,25,14,17,18,15,17],
    "semana 4":[25,24,20,25,24,20,21]
    }

ciudades={
    "Puyo": Puyo,
    "Baños": Baños,
    "Ambato": Ambato
}
a=0
#Bucle para asegurarse de que la ciudad que igrese este en el diccionario
while True:
    ciudad_eleg= str (input("Ciuadad que desea conocer:"))
    if ciudad_eleg in ciudades:
        break

#Funcion necesaria para que muestre la ciudad y las 4 semanas con el promedio de temperaturas
def temtotal():
    ciudadd=ciudades[ciudad_eleg][sema_eleg]

    b= 0
    for temperaturas1 in ciudadd:
        b += temperaturas1
        tem_promedio = b / 7
        tem_promedio1 = round(tem_promedio, 2)
    print (sema_eleg,":",tem_promedio1)

#Hacemos uso de la funcion reducion el temaño del programa
sema_eleg = "semana 1"
semana1= temtotal()
sema_eleg = "semana 2"
semana2= temtotal()
sema_eleg = "semana 3"
semana3= temtotal()
sema_eleg = "semana 4"
semana4= temtotal()


