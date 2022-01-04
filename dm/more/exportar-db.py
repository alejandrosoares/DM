'''
	Scripts para exportar los productos obtenidos mediante Web Scraping a la bd de la App Web
	Tareas para realizar:
	1- Armar las descripcion de los productos
	2- Armar la ruta de las imagenes para que Django las pueda encontrar
	3- Completar los campos con la informacion que todavia no tengo

'''
import sqlite3

pathBdApp = 'C:/DistribuidoraMarcia/dm/dm/db.sqlite3'
pathBdProducts = 'C:/Web-Scraping/Informacion-proveedores/productos.db'
PRODUCTS = []


def ShowItems(array):
	a = 0
	for x in array:
		print(f'{a} - {x}')
		a += 1


def codeGenerator(value):

	valueString = str(value)
	if len(valueString) == 1:
		return '00' + valueString
	elif len(valueString) == 2:
		return '0' + valueString
	else:
		return valueString


def Run():

	connectionApp = sqlite3.connect(pathBdApp)
	connectionProducts = sqlite3.connect(pathBdProducts)

	cursorApp = connectionApp.cursor()
	cursorProducts = connectionProducts.cursor()

	codeAndId = cursorApp.execute("SELECT * FROM products_codeproduct LIMIT 1").fetchone()
	products = cursorProducts.execute("SELECT * FROM duravit").fetchall()

	# ShowItems(codes)

	# (1, 'Juego de Té con Bandeja Duravit 500', 'Cod. 500', '300 x 300 x 700 mm', 'Duravit/nenas/juego-te-bandeja-500.jpg', 'nenas', 'Duravit')
	# Campos de la base de datos : id, code(string), name, description, price, img, stock, inStock


	# Verifico si la tabla tiene registros, para luego tomar el ultimo id y code para iniciar desde alli la insercion de registros
	if codeAndId == None:
		code = 0
		idItem = 0
		noneItem = True
	else:
		code = int(codeAndId[1])
		idItem = codeAndId[0]
		noneItem = False

	# Variable que no tengo
	stock = 10
	inStock = 1
	price = 105.50

	print("Iniciando la exportacion de los registros")
	for p in products:
		if p[3] != None:
			description = "Marca: " + p[6] + "; Tamaño: " + p[3] + "; Categorias: " + p[5].capitalize()
		else:
			description = "Marca: " + p[6] +"; Categorias:" + p[5].capitalize()
		pathImg = 'img/' + p[4]
		code += 1
		idItem += 1
		productCode = codeGenerator(code) 

		# Insertando los valores dentro de db de la App
		cursorApp.execute("INSERT INTO products_product (id, code, name, description, price, img, stock, inStock) VALUES ('" + str(idItem) + "','" +  productCode +\
			"','" + p[1] +"','" + description +"','" + str(price) +"','" + pathImg +"','" + str(stock) + "','" + str(inStock) +"')")

		
	# Actualizando/ creando los valores de lastIdItem y lastCodeItem de la tabla de products_codeproduct
	if noneItem:
		# Primero datos de la tabla
		cursorApp.execute("INSERT INTO products_codeproduct (lastIdItem, lastCodeItem) VALUES ('" + str(idItem)  + "','" + productCode +"')")
	else:
		# La tabla ya contiene datos
		cursorApp.execute("UPDATE products_codeproduct SET lastIdItem = '" + str(idItem) +"', lastCodeItem = '" + productCode + "' WHERE id=1")
		

	connectionApp.commit()

	connectionApp.close()
	connectionProducts.close()

	print("Finalizando la exportacion de los registros")



if __name__ == '__main__':
	Run()

