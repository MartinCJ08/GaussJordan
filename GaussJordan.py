from random import randint
fila = 3
col = fila+1
a = -9
b = 9 

def createMatrix(fila,col,a,b):
	if(fila == 0):
		print ("debe tener al menos una fila")
		matriz = [None]
	else:
		matriz = [None] * fila
		for i in range(fila):
			matriz[i] = [None] * col
		for i in range(fila):
			for j in range(col):
				matriz[i][j] = randint(a,b)
	return matriz	

def printMatrix(matriz):
	for i in range(len(matriz)):
		print(matriz[i])

def swap(matriz, fila,piv):
	temp = matriz[piv]
	if (piv == (fila-1)):
		print("No se puede")
	else:
		matriz[piv] = matriz[piv+1]
		matriz[piv+1] = temp
		doOne(matriz,piv,matriz[piv][piv],fila+1)
		doZero(matriz,piv,fila,fila+1)

def doOne(matriz,piv, a,col):
	if (a!=0):
		for j in range(col):
			matriz[piv][j] = matriz[piv][j]/a
	else:
		print ("No se puede dividir por cero")
		swap(matriz,col-1,piv)

def doZero(matriz, piv, fila,col):
	for i in range(fila):
		if (i!=piv):
			b = matriz[i][piv]
			for j in range(col):
				#b = matriz[i][piv]
				#print ("alv%s"%matriz[i][j])
				matriz[i][j] = matriz[i][j]-b*matriz[piv][j]
				#print ("compa%s"%matriz[i][j])

def testMatriz(matriz, fila,col):
	ban = True
	for i in range(fila):
		for j in range(col):		
			if(i==j and matriz[i][j] ==0):
				ban = False
	if(ban == False):
		print ("La matriz no tiene una solución única")

matriz = createMatrix(fila,col,a,b)
#matriz = [[2,2,4,6],[7,9,0,4],[1,2,0,3]] #Matriz inconscistente!!
#matriz = [[3,2,4,6],[7,0,3,4],[1,2,2,3]]
#matriz = [[0,2,0,3],[7,0,2,8],[6,3,8,9]]
print ("Matriz original")
printMatrix(matriz)

for i in range(fila):
  for j in range(col):
  	if(i==j):
  		a = matriz[i][j]
	  	doOne(matriz,i,a,col)
	  	doZero(matriz,i,fila,col)
	  	print("Hacer uno pivote, ceros arriba y abajo")
	  	printMatrix(matriz)	


print ("Matriz final")
printMatrix(matriz)
testMatriz(matriz,fila,col)