import numpy as np
import sys

def jacobi(itr, mat, mat_rta, x0):
  aux = np.diag(mat)
  resultante = mat - np.diagflat(aux)

  print("\nTABLA")
  for i in range(itr):
    x0 = (mat_rta - np.dot(resultante, x0)) / aux
    print("\nSolución ", i+1)
    print(x0)




while(1):
  itr = 10
  #matrices
  mat = np.array([[2, 0, -1], [4, 2, 1], [-1, 1, 1]])
  mat_rta = np.array([1, 2, 1])
  x0 = np.array([1, 2, 3])
  jacobi(itr, mat, mat_rta, x0) 
  sys.exit()