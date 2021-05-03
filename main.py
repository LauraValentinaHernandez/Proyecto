print("¡¡BIENVENIDO AL RESTAURANTE DE LA UNIVERSIDAD EAN!!")
nombre=input("Digite su nombre: ")
iden=input("Digite su numero de identificacion: ")
option1 = "Hamburguesa carne de res 100 gramos"
valoroption1 = 10000
option2 = "Perro caliente especial"
valoroption2 = 8000
option3 = "Empanada de carne o pollo"
valoroption3 = 3000
acompa1 = "Porcion de papas a la francesa"
valoracompa1 = 3500
acompa2 = "Aros de cebolla"
valoracompa2 = 4000
acompa3 = "Nuggets"
valoracompa3 = 5000

esvalido = False

orden = "Su orden es: "
total = 0

print("Estamos felices de tenerte aqui, ", nombre, "a cotinuacion el menu con nuestros productos")
print("Combo 1: " + option1)
print("Combo 2: " + option2)  
print("Combo 3: " + option3)

while esvalido == False:
  pedido=int(input("Por favor digita el numero de combo que vas a pedir ( 1, 2 o 3): "))

  if pedido == 1:
    orden = orden + option1
    total = total + valoroption1
    esvalido = True
  elif pedido == 2:
    orden = orden + option2
    total = total + valoroption2
    esvalido = True
  elif pedido == 3:
    orden = orden + option3
    total = total + valoroption3
    esvalido = True
  else:
    print("invalida")

esvalido = False

print("Acompañamiento 1: " + acompa1)
print("Acompañamiento 2: " + acompa2)
print("Acompañamiento 3: " + acompa3)


while esvalido == False:
  acompa=int(input("Por favor digita el acompañamiento que vas a pedir (ejemplo 1, 2 o 3): "))

  if acompa == 1:
    orden = orden + " y " + acompa1
    total = total + valoracompa1
    esvalido = True
  elif acompa == 2:
    orden = orden + " y " + acompa2
    total = total + valoracompa2
    esvalido = True
  elif acompa == 3:
    orden = orden + " y " + acompa3
    total = total + valoracompa3
    esvalido = True
  else:
    print("invalida")

print(orden)
print("El total es: " + str(total))
print("Estamos felices de antenderte, ¡Vuelve pronto!")

#inventario


producto1 = "Carne de hamburguesa, codigo: 1 = "
producto2 = "Pan de hamburguesa, codigo: 2 = "
producto3 = "Lechuga, codigo: 3 = "
producto4 = "Tomate, codigo: 4 = "
producto5 = "Salsa tomate, codigo: 5 = "
producto6 = "Pan para perro caliente, codigo: 6 = "
producto7 = "Salchicha, codigo: 7 = "
producto8 = "Papas fosforo, codigo: 8 = "
producto9 = "Papa francesa, codigo: 9 = "
producto10 = "Empanada de carne, codigo: 10 = "
producto11 = "Empanada de pollo, codigo: 11= "
producto12 = "Botella de gaseosa, codigo: 12 = "
producto13 = "Aros de cebolla, codigo: 13 = "
producto14 = "Nuggets, codigo: 14 = "

print("Productos: " + producto1+producto2+producto3+producto4+producto5+producto6+producto7+producto8+producto9+producto10+producto11+producto12+producto13+producto14)
producto=int(input("Por favor digite el codigo que quiere modificar: "))
cantidad=int(input("Por favor digite cantidad: "))






  
  