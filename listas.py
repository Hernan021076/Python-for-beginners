# FUNCIONES

demo_list = [1, "hello", 1.34, True, [1, 2, 3]]
colors = ['red', 'green', 'blue']

numbers_list = list((1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
print(type(numbers_list))
print(colors)
print(demo_list)

# FUNCION LISTA - list

r = list(range(1, 10))
r1 = list(range(1, 100))

# numbers_list(1, 2, 3, 4, 5, 6)  # Esta línea no es necesaria y debe ser comentada

print(numbers_list)  # Aca me lista el arreglo completo, es decir desde 1 a 10
print(r)  # Aca a diferencia de numbers_list, se listan los 10 numeros de mi range, pero como arranca contando desde el cero, solo llega a 9

print(type(colors))
print(r1)
################################################################
print("_____________________________________________________________")
#

# Verificar si "green" está en la lista colors
if "green" in colors:
    print("El color green está en la lista.")
else:
    print("El color green no está en la lista.")

