import numpy as np
import math

def fx(x,indicador):  
  if(indicador==1):
    return x**3+2x+math.sqrt(3+2)
  if(indicador==2):
    return np.log(x**2+2)
  if(indicador==3):
    return np.exp(x)-x-1

def punto_1(tol, k):
    x=0
    p1=fx(x, 1)
    
    
    
def punto_2(tol, x0, p3):
    x=0
    p1=fx(x, 2)
    iter=51
    
    
    

def punto_3(x0):
    x=0
    p1=fx(x, 3)
    p2=np.log(x+1)
    iter=50
    xtol=-8
    x = float(x0) 
    for i in range(iter):
        dp = -p1 / p2
        x = x + dp
        if abs(dp / x) < xtol:
            print("El valor de x, tal que f(x)=0 es: {} " x)
            print("Las iteraciones fueron: ", i)
            print("\n")  
        


while(1):
    print("\nParcial Andres Alarcon. 3 es el numero al final de mi cedula")
    print("\nEliga el ejercicio")
    print("\n")
    print("\n1. 1a")
    print("\n2. 2a")
    print("\n3. 4")
    opcion==int(input())
    
    if opcion==1:
        tol=-16
        k=math.sqrt(3+2)
        punto_1(tol, k)
    elif opcion==2:
        tol=-8
        x0=1
        p3=1.5111
        punto_2(tol, x0, p3)
    elif opcion==3:
        x0=1
        punto_3(x0)
    
