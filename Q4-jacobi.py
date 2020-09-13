from __future__ import division
import numpy as np
from numpy import linalg

def jacobi(A,b,x0,tol,N):
  #preliminares
  A = A.astype('double')
  b = b.astype('double')
  x0 = x0.astype('double')
  n=np.shape(A)[0]
  x = np.zeros(n)
  it = 0
  #iteracoes
  while (it < N):
    it = it+1
    #iteracao de Jacobi
    for i in np.arange(n):
      x[i] = b[i]
      for j in np.concatenate((np.arange(0,i),np.arange(i+1,n))):
        x[i] -= A[i,j]*x0[j]
      x[i] /= A[i,i]
    #tolerancia
    if (np.linalg.norm(x-x0,np.inf) < tol):
      return x
#prepara nova iteracao
    x0 = np.copy(x)
  raise NameError('num. max. de iteracoes excedido.')

A=np.array(([10,2,2],[1,10,2],[2,-7,-10]))
b=np.array(([28,7,-17]))
x0=np.array(([0,0,0]))
tol=0.0001
N=50

x = jacobi(A,b,x0,tol,N)
print(x)
input("Tecle enter para finalizar!")