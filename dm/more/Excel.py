import pandas as pd
import xlrd

'''
df = pd.read_excel('Productos.xlsx', sheet_name='Sheet2')

print(df)
'''
doc = xlrd.open_workbook('Productos.xlsx')

hoja = doc.sheet_by_index(3)


filas = hoja.nrows
columnas = hoja.ncols
print(type(filas))

for f in range(filas):
	# name = hoja.row(f)[5]
	name = hoja.cell_value(f, 5)
	#print(name)
	print(hoja.row(f))
	'''
	print(hoja.row(f)[5])
	if "text:" in hoja.row(f)[5]:
		hoja.row(f)[5]
	'''