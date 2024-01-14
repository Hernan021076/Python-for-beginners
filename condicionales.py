# IF -  else
hora = 19
if hora < 12:
    print("Buenos dias")
elif hora < 18: #SIno si
    print("Buenas tardes")
else:
    print("Buenas nocehes")

#WHILE (Mientras)
    
contador = 0

while contador < 5: #Mientras el contador sea menor a 5, ejecute todo lo que esta dentro del While, cuando supere a 5 salga
    print("El contador es: ", contador)
    contador +=1

frutas = ["manzana", "banana", "pera", "pomelo", "durazno"]
print(frutas[2]) #Lo que saldra por terminal seria pera, recordar que arranca desde 0 la posicion de un array

#FOR

for fruta in frutas:
    print(fruta)

# INGRESO DE ALGO POR PARTE DEL USIARIO - input

age = input("Ingrese su edad: ")
new_age = int(age) +5
print("Su nueva edad la ultima semana despues del DNU del animal de Miley es: ", new_age)

                