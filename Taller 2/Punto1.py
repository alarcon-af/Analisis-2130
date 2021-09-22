#Punto 1

import numpy as np 

mat_A= np.array([[1, 0, 1], #La posición 1,3 cambia de valor de 0 a -2 para el punto D
                 [1,  4, 0],
                 [2, 0,  3]])

b  = np.array([2,5,0])

x = np.zeros_like(b)

tol = 1e-6
maxIter = 100
aux = 0

for a in range(maxIter): 
    for i in range (len(b)): 
        x[i] = (b[i]-np.sum(mat_A[i][:i]*x[:i])-np.sum(mat_A[i][i+1:]*x[i+1:]))/mat_A[i][i] 
            
    e = np.linalg.norm(mat_A@x-b)
    
    if(e<tol):
        break; 
    
    #print(a,x)
    aux = a
    
    
print(" ")
print ("Por Gauss Sidel: ") 
print(a,x)
print(" ")    
print("#########################")  
print("VERIFICACI�N POR LIBRERIA NUMPY")
f = np.linalg.solve(mat_A,b)
print(f)

#JACOBI#
def Jacobi(A,b,x0,tol,n):
    D = np.diag(np.diag(mat_A))
    LU = A- D
    x = x0
    
    for i in range (n): 
        D_inv=np.linalg.inv(D)
        xtemp=x
        x= np.dot(D_inv,np.dot(-LU,x))+np.dot(D_inv,b)
        print("jacobi:", x )
        if np.linalg.norm(x-xtemp)<tol:
            return x
    return x
        
##Llamado a jacobi
print(" ")
jaco = Jacobi(mat_A, b, x, tol, maxIter)
print("Con jacobi el resultado es: ", jaco)
print("El metodo de Jacobi converge debido a que la matriz es diagonalmente dominante, esto debido a las operaciones de matriz realizadas para que cumpliera esta condicion")





