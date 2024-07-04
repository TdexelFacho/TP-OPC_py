lista = []
print(f"{lista}")
while True:
 opcion = input ("Desea ingresar un producto S/N")
 if opcion == ("S"):
   producto=input("Ingrese el producto")
   lista.append(producto)
   print(lista)
   Sacar= input("Desea quitar un producto S/N")
   if Sacar== ("S"):
    sacar = input("Escriba el elemento que desea sacar:")
    lista.remove(sacar)
    print(lista)
 else:
   if opcion == ("N"):
     print(f"{lista} lISTA FINALIZADA")