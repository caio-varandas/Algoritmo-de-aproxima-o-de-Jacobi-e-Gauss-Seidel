import numpy as np

def jacobi(A, b, x0=0, tolerancia=1e-10, max_iter=100):
    n=len(b)
    x=np.zeros(n) if x0==0 else x0 #vetor com xn's inicialmente zerado
    D=np.diag(A) #pega a diagonal principal
    R=A-np.diagflat(D) #cria uma matriz e zera a diagonal principal
    iteracoes=0
    while iteracoes<max_iter:
        #np.dot faz o calculo da multiplicacao da matriz R pelo vetor x
        x_novo=(b-np.dot(R, x))/D
        iteracoes+=1

        if np.allclose(x, x_novo, atol=tolerancia): #verifica se a solucao converge dentro da tolerancia dada
            #np.allclose compara x com x_novo e ve se ops dois sao menores que a tolerancia
            print(f"Convergiu após {iteracoes} iterações.")
            return x_novo
        x=x_novo
    print("O método de Jacobi não convergiu após 100 iterações.")
    return x 



linhas=int(input("Numero de linhas:"))
colunas=int(input("Numero de colunas:"))
matriz=[]

for i in range(linhas):
    linha=list(map(int, input().split())) #leitura da linha
    matriz.append(linha)

matriz = np.array(matriz, dtype=float)  #conversão de um array em Numpy

A=matriz[:, :-1] #todas as colunas exeto a ultima
b=matriz[:, -1] #somente a ultima coluna

solucao=jacobi(A, b)
print("Solução aproximada:", solucao)


