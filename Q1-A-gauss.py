"""
Eliminação de Gauss sem pivot resolve Mx=d
"""
import numpy as np

def gaussElim(M,d):
    A=np.copy(M) #evita a alteração da matriz de coeficientes, copiando-a
    b=np.copy(d) #idem para os termos independentes
    x=np.zeros(b.shape)
    Ash=A.shape;
    n=Ash[0];n2=Ash[1]
    Bsh=b.shape
    n3=Bsh[0]
    if n!=n2 or n3!=n or len(Bsh)!=1 or len(Ash)!=2:
        print('Erro de dimensão')
        x=float('nan')
        return x
    #triangulação
    for k in range(0,n-1):
        if A[k,k]==0:
            x=float('nan')
            return x
        for j in range(k+1,n):
            e=A[j,k]/A[k,k]
            for m in range(k+1,n):
                A[j,m]=A[j,m]-e*A[k,m]
            b[j]=b[j]-e*b[k]
    #substituição
    for k in range(n-1,-1,-1):#=n:-1:1 %indice regressivo
        sum=0.
        for j in range (k+1,n):
            sum=sum+A[k,j]*x[j]

        x[k]=(b[k]-sum)/A[k,k]
    return x


A=np.array(([20,7,9],[7,30,8],[9,8,30]))
b=np.array(([16,38,38]))
x=gaussElim(A,b)
print('x=', x)

input("Tecle enter para finalizar!")