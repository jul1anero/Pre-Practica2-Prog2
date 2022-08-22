#Crear un programa que permita ingresar una lista de numeros al usuario y muestre por pantalla el maximo entre ambos numeros.

#Nota : Hacerlo con la función max(a,b) y luego con una comparación

#INICIO
print("ingrese un numero")
a = input()
print("ingrese otro numero")
b = input()
mayor= max(a,b)
print("el mayor es",mayor)
if a > b:
    print("el mayor es el primero", a)
else:
    print("el mayor es el segundo",b)

#FIN