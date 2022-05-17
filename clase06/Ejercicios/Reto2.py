
# #Esta función debe retornar un nuevo diccionario con las llaves nombre,
# edad, atracción, primer_ingreso, total_boleta y apto del cliente:
# • En donde apto tendrá como valor una variable booleana, será verdadera
# si su edad cumple con los rangos exigidos en la tabla anterior, en el
# caso contrario será falsa.
# • En el caso de atraccion y total_boleta, si no se cumple el rango de
#  edades se le asignara un valor de ‘N/A’ a cada uno.
# • Si primer_ingreso es verdadero, el total_boleta será el valor
#  de la boleta menos el descuento de lo contrario se pagará el valor
#  neto de la boleta.

datos = {
  "id_cliente": int, 
  "nombre": str, 
  "edad": int, 
  "Atracción": str,
  "Apto_Cliente": bool,
  "primer_ingreso": bool,
  "Total_Boleta": Total_boleta  
}

#datos["id_cliente"] = "100121"
#print (datos)


def aventuras_extremas(datos: dict):
  if (datos["edad"]) >= 7:
    datos["Apto_Cliente"] = True

  else:
    datos["Apto_Cliente"] = False
    datos["Atracción"] = "N/A"
    datos["Total_boleta"] = "N/A"
  if 

  

    
  

 