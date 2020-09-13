import numpy as np

def fatoraLU(A):
  U = np.copy(A)
  n = np.shape(U)[0]
  L = np.eye(n)
  for j in np.arange(n-1):
    for i in np.arange(j+1,n):
      L[i,j] = U[i,j]/U[j,j]
      for k in np.arange(j+1,n):
        U[i,k] = U[i,k] - L[i,j]*U[j,k]
      U[i,j] = 0
  return L, U

A=np.array(([20,7,9],[7,30,8],[9,8,30]))

l, u = fatoraLU(A)
print(l)
print(u)
input("Tecle enter para finalizar!")