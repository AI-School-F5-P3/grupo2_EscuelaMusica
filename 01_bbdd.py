import mysql.connector

conexion1=mysql.connector.connect(host="localhost",port=3206, user="root", passwd="", db="armonia_academy") #Hay que especificar el puerto porque por defecto suele ser 3306 y no 3206
cursor1=conexion1.cursor()      

#cursor1.execute("drop database if exists academy_armonia;")
#cursor1.execute("CREATE database academy_armonia character set latin1 collate latin1_spanish_ci;")
cursor1.execute("USE armonia_academy;")


#  Para ver en python el contenido de las tablas

cursor1.execute('SELECT * FROM teacher; ')   

longitud = 0
tabla = list()
for fila in cursor1:
    ancho = len(fila)
    tabla.append(fila)
    longitud += 1

for i in range(longitud):
    linea = ""
    for j in range(ancho):
        linea = linea + str(tabla[i][j]) + "\t"
    print(linea)
  
conexion1.close()
