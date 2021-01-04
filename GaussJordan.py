from random import randint

def createMatrix(fila,col,a,b):
  """
  Function description: Create and populate a matrix
  Parameters:
  fila - Number of rows
  col  - Number of cols
  a    - Lower limit to randomize
  b    - upper limit to randomize
  Returns: 
  """
  if fila <= 0 or col <= 0:
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
  """
  Function description:
  Parameters:
  Returns:
  """
  for i in range(len(matriz)):
    print(matriz[i])

def swap(matriz, fila,piv):
  """
  Function description:
  Parameters:
  Returns:
  """
  temp = matriz[piv]
  if piv == (fila-1):
    print("No se puede")
  else:
    matriz[piv] = matriz[piv+1]
    matriz[piv+1] = temp
    doOne(matriz,piv,matriz[piv][piv],fila+1)
    doZero(matriz,piv,fila,fila+1)

def doOne(matriz,piv, a,col):
  """
  Function description:
  Parameters:
  Returns:
  """
  if a != 0:
    for j in range(col):
      matriz[piv][j] = matriz[piv][j]/a
  else:
    print ("No se puede dividir por cero")
    swap(matriz,col-1,piv)

def doZero(matriz, piv, fila,col):
  """
  Function description:
  Parameters:
  Returns:
  """
  for i in range(fila):
      if (i!=piv):
          b = matriz[i][piv]
          for j in range(col):
              matriz[i][j] = matriz[i][j]-b*matriz[piv][j]

def testMatriz(matriz, fila,col):
  """
  Function description:
  Parameters:
  Returns:
  """
  ban = True
  if (fila + 1) == col:
    for i in range(fila):
      for j in range(col):
          if i==j and matriz[i][j] == 0:
              ban = False
  else:
    ban = False

  return ban

def getGaussJordanMatrix(matriz, fila, col, debug):
  """
  Function description:
  Parameters:
  fila - Number of rows
  col  - Number of cols
  Returns:
  """
  for i in range(fila):
    for j in range(col):
        if i == j:
            a = matriz[i][j]
            doOne(matriz,i,a,col)
            doZero(matriz,i,fila,col)
            if debug == 1:
              print("Hacer uno pivote, ceros arriba y abajo")
              printMatrix(matriz)

def main():
  fila = 3
  col = fila+1
  a = -9
  b = 9
  #matriz = createMatrix(fila,col,a,b)
  #matriz = [[2,2,4,6],[7,9,0,4],[1,2,0,3]] #Matriz inconscistente!!
  #matriz = [[3,2,4,6],[7,0,3,4],[1,2,2,3]] #Matriz inconscistente!!
  #matriz = [[0,2,0,3],[7,0,2,8],[6,3,8,9]] #Matriz inconscistente!!
  matriz = [[2,6,1,7],[1,2,-1,-1],[5,7,-4,9]]
  print ("Matriz original")
  printMatrix(matriz)

  isCandidateMatrix = testMatriz(matriz,fila,col)

  if isCandidateMatrix:
    getGaussJordanMatrix(matriz, fila, col, 1)
  
    print ("Matriz final")
    printMatrix(matriz)
  else:
    print("No es posible aplicar el método Gauss-Jordan para la matriz introducida")
    
if __name__ == "__main__":
  main()