#funcion de saludo.
def saludar():
	print ("Hola, bienvenido a mi primer programa de funciones!")

#Funcion de multiplicacion.
def multi():
	print("Escribe un numero: ")
	numX = float(input())
	print("Escribe un segundo numero: ")
	numY = float(input())
	result = numX * numY
	print ("El resultado de la multiplicacion es: "+str(result))

#funcion de división
def division():
	print("Escribe un numero: ")
	numX = float(input())
	print("Escribe un segundo numero: ")
	numY = float(input())
	if (numY or numX == 0):
		print ("Syntax error")
	else:
		result = numX / numY
		print ("El resultado de la division es: "+str(result))

#funcion de potencia
	numX = float(input())
	print("Escribe un numero: ")
def pot():
	result = numX * numX
	print ("El cuadrado de tu numero es: "+str(result))

#Funcion principal de mi programa.
def main():
	saludar ()
	print()

	print ("Escribe 1 si quieres multiplicar.")
	print ("Escribe 2 si quieres dividir.")
	print ("Escribe 3 si quieres saber el cuadrado del numero.")
	num1 = int(input())
	#Aquí vamos a usar if's. Dependiendo del numero que ponga el usuario lo llevara a las funciones correspondientes
	if (num1 == 1):
		multi ()
	if (num1 == 2):
		division ()
	if (num1 == 3):
		pot()
if __name__ == "__main__":
	main()