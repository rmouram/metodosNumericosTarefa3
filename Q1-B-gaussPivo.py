#!/usr/bin/env python
#-*- coding: utf-8 -*-
 
import numpy as np
 
def pivo(k, b, A):
    n = len(b)
    jmax = k
    for j in range(k+1, n, 1):
        if ( np.abs(A[j][k]) > np.abs(A[jmax][k]) ):
            jmax = j
 
    TempA       = np.zeros_like(b)
    TempA[:]    = A[k][:]
    A[k][:]     = A[jmax][:]
    A[jmax][:]  = TempA[:]
   
    TempB  = b[k]
    b[k]   = b[jmax]
    b[jmax] = TempB
   
    return A, b

def superior(A, b):
    Ln = len(b)
    cn = Ln
    for Li in range(0, Ln-1, 1):
        A[:], b[:] = pivo(Li, b, A)
        for Lj in range(Li+1, Ln, 1):
            lam   =  A[Lj][Li] /A[Li][Li]
            b[Lj] = b[Lj] - b[Li] * lam
            for ci in range(Li, cn, 1):
                A[Lj][ci] =  A[Lj][ci] - A[Li][ci] * lam
    return (b, A)

def retrosub(b, A):
  n = len(b)
  x = np.zeros_like(b)
  x[n-1] = b[n-1] / A[n-1][n-1]
   
  for i in range(n-2, -1, -1):
    soma = b[i]
    for j in range(i+1, n, 1):
      soma = soma - A[i][j]*x[j]
    x[i] = soma / A[i][i]
     
  return x


A=np.array(([20,7,9],[7,30,8],[9,8,30]))
b=np.array(([16,38,38]))
 

b, A = superior(A, b)
x = retrosub(b, A)

print(A)

print ('\nSolução:')
print ('x1 =', x[0])
print ('x2 =', x[1])
print ('x3 =', x[2])

input("Tecle enter para finalizar!")