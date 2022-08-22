#Crear un programa que permita al usuario ingresar una lista de numeros. De esa lista de numeros almacenar en otra lista los numeros impares.

#El programa debe de mostrar por pantalla la lista de numeros originales y la lista de numeros impares.

#INICIO
listaNumeros=[]
listaImpares=[]
numeroUsuario = int(input("Intoroduca un numero: "))
listaNumeros.append(numeroUsuario)
decision = input("Introcudir otro?: ")
while decision == "s" or decision == "S":
    numeroUsuario = int(input("Intoroduca otro numero: "))
    listaNumeros.append(numeroUsuario)
    decision = input("Introcudir otro?")

for x in listaNumeros:
    if x % 2 !=0:
        listaImpares.append(x)

print("los impares son", listaImpares)
#FIN