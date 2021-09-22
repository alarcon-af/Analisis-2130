import numpy as np
from scipy.sparse.linalg import cg
import time


def gradienteConjugado(A, b, x=None):
    l = len(b)
    if not x:
        x = np.ones(l) 
    r = np.dot(A, x) - b
    p = - r
    r_k_norm = np.dot(r, r)
    for i in range(2*l):
        Ap = np.dot(A, p)
        alpha = r_k_norm / np.dot(p, Ap)
        x += alpha * p
        r += alpha * Ap
        r_kplus1_norm = np.dot(r, r)
        beta = r_kplus1_norm / r_k_norm
        r_k_norm = r_kplus1_norm
        if r_kplus1_norm < 1e-5:
            print ('Iteraciones:', i)
            break
        p = beta * p - r
    return x

if __name__ == '__main__':
    n = 2000
    P = np.random.normal(size=[n, n])
    A = np.dot(P.T, P) 
    b = np.zeros(n) 
    
    np.set_printoptions(precision = 10)
    
    t1 = time.time()
    print ('Metodo 1.') #Metodo implementado aquí, no incluye una matriz dispersa
    x = gradienteConjugado(A, b)
    t2 = time.time()
    print ("tiempo: ",t2 - t1)
    print ('\nMetodo 2.') #Metodo de librería que soluciona sistemas de ecuaciones, no usa gradiente conjugado
    x2 = np.linalg.solve(A, b)
    t3 = time.time()
    print ("tiempo: ",t3 - t2)
 