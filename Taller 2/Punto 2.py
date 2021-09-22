#Punto 2
#Método de Gauss Sidel para solucion de sistemas de ecuaciones

import numpy as np 

#Declaracion de la matriz A

mat_A= np.array([[4 , 3, 0], #La posición 1,3 cambia de valor de 0 a -2 para el punto D
                 [3,  4, -1],
                 [0, -1,  4]])

####CALCULO DEL RADIO ESPECTRAL####PUNTO B

Mat_diag = np.array([[ 4, 0., 0.],[ 0., 4, 0.],[ 0., 0., 4]])
Mat_sup = np.array([[ 4., 3, 0.],[ 0., 4, -1],[ 0., 0., 4]])
Mat_inf = np.array([[ 4, 0., 0.],[ 3, 4, 0.],[ 0., -1, 4]])

U = Mat_sup - Mat_diag
M = np.dot(np.linalg.inv(Mat_inf),U);M

print("Radio espectral",np.max(abs(np.linalg.eigvals(M))))

#Declaracion de b para el punto c
b  = np.array([0.254,-1.425,2.978])

x = np.zeros_like(b)

tol = 1e-16
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


#Punto D es una modificacion al C 


        
    

