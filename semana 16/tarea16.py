file=open('mis_notas.txt',"w")

file.write("Primera linea.\nSegunda linea.\nTercera linea.\n")

file.close()

file=open('mis_notas.txt',"r")
linea1= file.readline()
linea2= file.readline()
linea3= file.readline()

print("Lineas del archivo")
print("Linea1:",linea1,"Linea2:",linea2,"linea3:",linea3)

