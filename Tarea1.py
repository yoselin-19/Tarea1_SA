import requests
import json

# Funcion que permite obtener el token de autorizacion
def GetToken(grant_type, client_id, client_secret):
	#Recursos necesarios para realizar la peticion
	url = 'https://api.softwareavanzado.world/index.php'
	argumentos = { 'option' : 'token', 'api': 'oauth2'}
	payload = { 'grant_type' : grant_type, 'client_id': client_id, 'client_secret': client_secret}
	headers = { 'Content-Type': 'application/json'}

	# Haciendo peticion al servidor
	response = requests.post(url, params = argumentos, json=payload, headers = headers)

	# Si se obtiene una respuesta OK, retornar el token
	if response.status_code == 200:
		response_json = response.json() #La variable response_json Es un diccionario

		# Se obtiene el token del diccionario que nos devuelve
		access_token = response_json['access_token']

		# Retorno valor del token
		return access_token

	else:
		print('No se pudo obtener el token, credenciales invalidas')
		return None


# Funcion que permite listar los contactos de la aplicacion
def listar_Contactos(access_token):
	#Recursos necesarios para realizar la peticion
	url = 'https://api.softwareavanzado.world/index.php?webserviceClient=administrator&webserviceVersion=1.0.0&option=contact&api=hal'
	args = { 'list[limit]': '0', 'access_token': access_token}
	headers = { 'Content-Type': 'application/json'}

	# Haciendo peticion al servidor
	response = requests.get(url, params=args, headers = headers)

	# Empezar a listar los contactos existentes
	print('*************** Start Listar ***************')
	if response.status_code == 200:
		response_json = response.json() #La variable response_json Es un diccionario
		
		# Se obtiene la lista de contactos
		contactos = response_json['_embedded']['item']

		if contactos:

			# Por cada contacto se imprime su id y su nombre
			for contacto in contactos:
				id_ = contacto['id']
				nombre = contacto['name']

				# Generando cadena de salida por cada contacto encontrado
				contacto_data = "ID: {0}, Name: {1}"
				print(contacto_data.format(id_, nombre))

	print('*************** End Listar ***************')


# Funcion que permite crear los 10 clientes solicitados, segun las instrucciones
def crear_Contactos(access_token):
	#Recursos necesarios para realizar la peticion
	url = 'https://api.softwareavanzado.world/index.php?webserviceClient=administrator&webserviceVersion=1.0.0&option=contact&api=hal'
	args = {'access_token': access_token}
	headers = { 'Content-Type': 'application/json'}

	# Empezar a crear los contactos
	print('*************** Start Crear contactos ***************')

	NContactos = 1
	while NContactos < 11:
		nombre = "Yoselin-201403819_No_" + str(NContactos)
		payload = { "name": nombre, "catid": NContactos }

		# Haciendo peticion al servidor
		response = requests.post(url, params = args, json=payload, headers = headers)

		if response.status_code == 200:
			# Generando cadena de salida por cada contacto creado
			print(payload)

		# Update contador
		NContactos+=1

	print('*************** End Crear contactos ***************')


# main, de la aplicacion
if __name__ == '__main__':

	# Obtener el token de autenticacion para utilizar las funciones posteriores
	access_token = GetToken('client_credentials', 'annelice119@gmail.com', '201403819')

	# Si se logra obtener el token, ingresar al menu de opciones
	if access_token != None:

		# Menu de opciones de la aplicacion
		opcion = 0
		while opcion != 3:
			opcion = int(input("Que desea hacer:\n" + 
							"1. Listar\n" + 
							"2. Crear 10 usuarios\n" + 
							"3. Salir\n"
							"R: "))
			if opcion == 1:
				# Llamar a la funcion que lista los contactos
				listar_Contactos(access_token)
			elif opcion == 2:
				# Llamar a la funcion que crea los 10 contactos
				crear_Contactos(access_token)

		# Salir de la aplicacion
		print("Exit")