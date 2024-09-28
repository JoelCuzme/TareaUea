informacion_personal={
    "Nombre":"Joel",
    "Edad": "18",
    "Ciudad": "Puyo",
}
#Original
print("Diccionario Original")
print(informacion_personal)

informacion_personal["Ciudad"]="Baños"
informacion_personal["Profesion"]="Estudiante"

#Modificado
print("Diccionario Modificado")
print(informacion_personal)

#Se evalua si existe la clave y se presgunta si se desea agrefarla
a= "diccionario Modificado con el numero de telefono"
print(a.title())
if "Telefono" in informacion_personal:
    print(informacion_personal)

else:
    v_tel= input("desea agragar el telefono, digite SI o NO: ")
    v_tel2= v_tel.upper()
    if v_tel2=="SI":
        telefono=  str(input("digite el telefono "))
        informacion_personal["Telefono"]=telefono
        print(informacion_personal)
    else:
        print(informacion_personal)

#Eliminamos una clave
print("Diccionario eliminado con una clave")
del informacion_personal["Edad"]
print(informacion_personal)

