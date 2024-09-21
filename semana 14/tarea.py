def calcular_descuento(val_total, descuento=10):
    total=val_total*(descuento/100)
    print("Porcentaje de descuento:",descuento,"%")
    print ("Total de descuento:", total,"USD")
    print("Total a pagar:",(val_total-total),"USD")
#bucle para asegurar que se coloquen los datos requeridos
while True:
    try:
        compra_total = int(input("Valor a cancelar: "))
        break
    except ValueError:
        print("Datos no validos")

while True:
    try:
        por= int(input("valor de descuento: "))
        break
    except ValueError:
        print("Datos no validos")

#primera llamada
calcular_descuento(compra_total, por)
while True:
    try:
        compra_total = int(input("Valor a cancelar: "))
        break
    except ValueError:
        print("Datos no validos")


#segunda llamada
calcular_descuento(compra_total,)



