from time import sleep
import re
import argparse

class color:
	VERDE = '\033[92m'
	END = '\033[0m'

def argumentos():
	parser = argparse.ArgumentParser(description="Introduzca una palabra a cifrar ")
	parser.add_argument('-e',dest="mode",help="Especifique el modo ",required=True)
	parser.add_argument('-p',dest="palabra",help="Especifique la palabra a cifrar",required=True)
	parser.add_argument('-n',dest="nk",help="numero de veces a cifrar",required=True)
	parser.add_argument('-k',dest="key",help="numero clave",required=True)
	arguments = parser.parse_args()
	return arguments
		

def cifrado_cesar(cadena,modo,key):
	abc = 'abcdefghijklmnopqrstuvwxyz'
	cadena_cifrar =''
	cadena = cadena.lower()
	for i in cadena:
			if i in abc:
				num = abc.find(i)
				if modo == 'cifrar':
					num = num+key
				elif modo == 'descifrar':
					num = num-key
				if num >= len(abc):
					num = num-len(abc)
				elif num < 0:
					num = num+len(abc)
				cadena_cifrar = cadena_cifrar+abc[num]
			else:
				cadena_cifrar = cadena_cifrar+i
	return cadena_cifrar

def main():
	argumentos()
	cadena = argumentos().palabra
	if not (re.match("[0-9]",cadena)):
		modo = argumentos().mode
		key = argumentos().key
		key = int(key)
		n = argumentos().nk	
		n = int(n)
		i = 1
		cadena2 = cadena
		while i<=n:
			if i>1:
				texto_cifrado =cifrado_cesar(texto_cifrado,modo,key)
			else:
				texto_cifrado =cifrado_cesar(cadena2,modo,key)
			cadena2=texto_cifrado
			i=i+1

		if modo == 'cifrar':
			print("La cadena descifrada es: ",cadena2)
		elif modo == 'descifrar':
			print("La cadena cifrada es: ",cadena2)
	else:
		sleep(2)
		print(color.VERDE,"Por favor, Introduzca solo letras no numeros. No sea cabron",color.END)

if __name__ == '__main__':
	main()
