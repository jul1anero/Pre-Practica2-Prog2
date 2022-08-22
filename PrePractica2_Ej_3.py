#Crear un programa que utilice la estructura try - catch. El usuario debe de ingresar dos numeros y mostrar por pantalla
#el resultado de la división entre ambos numeros. 

#En caso de que el divisor sea 0 utilizar la excepción ZeroDivisionError y mostrar el error por pantalla.


#INICIO
print("ingrese un numero:")
a = float(input())
print("ingrese otro numero:")
b = float(input())
try:
    resultado = a/b
    print("el resultado es", resultado)
except ZeroDivisionError as exception:
    print("el divisor no puede ser cero")
#FIN