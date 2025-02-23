import numpy as np 

def gaussSeidel(A, b, x0=None, tolerancia=1e-10, max_iter=100):#A matriz A de coeficientes, o vetor b de constantes, o vetor x0 é o chute inicial, a tolerância é o criterio de parada e o número máximo de iterações são passados como argumentos
    n=len(b)#Tamanho de acordo com o numero de linhas)
    x=np.zeros(n) if x0 is None else x0  # vetor com xn's inicialmente zerado
    iteracoes=0
    while iteracoes<max_iter:#Enquanto o número de iterações já realizadas for menor que o número máximo de iterações
        vetorIncognitas=np.copy(x)
        for i in range(n):
            s1=np.dot(A[i, :i], vetorIncognitas[:i])#Calcula a soma dos elementos da linha i da matriz A até a coluna i multiplicados pelos elementos do vetor vetorIncognitas até a posição
            s2=np.dot(A[i, i+1:], x[i+1:])#Calcula a soma dos elementos da linha i da matriz A a partir da coluna i+1 multiplicados pelos elementos do vetor x a partir da posição i+1
            vetorIncognitas[i]=(b[i]-s1-s2)/A[i, i]#Calcula o novo valor de x[i] utilizando a fórmula de Gauss-Seidel
        
        if np.allclose(x, vetorIncognitas, atol=tolerancia):#Verifica se a solução converge dentro da tolerância dada
            print(f"Convergiu após {iteracoes+1} iterações.")
            return vetorIncognitas#Retorna o vetor vetorIncognitas
        x=vetorIncognitas#Copia o vetor vetorIncognitas para x
        iteracoes+=1

    print("O método de Gauss-Seidel não convergiu após 100 iterações.")#Se o número de iterações for igual ao número máximo de iterações, imprime que o método não convergiu
    return x

def verificarDiagonalP(A):
    n=A.shape[0]
    for i in range(n):
        diag=abs(A[i, i])#Pega o valor absoluto do elemento da diagonal principal
        somaLinha=np.sum(np.abs(A[i, :]))-diag#Calcula a soma dos valores absolutos dos elementos da linha i da matriz A, subtrai o valor da diagonal principal
        if diag<somaLinha:#Se o valor da diagonal principal for menor que a soma dos outros elementos da linha
            return False
    return True

linhas=int(input("Número de linhas: "))
matriz=[]

#Utilizando desta forma não é necessário informar o número de colunas pois o programa irá identificar automaticamente o número de colunas a partir da primeira linha informada
for i in range(linhas):
    linha=list(map(int, input().split()))
    matriz.append(linha)#Adiciona a linha na matriz

matriz=np.array(matriz, dtype=float)  # conversão de um array em Numpy

#Basicamente a formação de Ax=b, onde A é a matriz, x é o vetor de incógnitas e b é o vetor de resultados
A = matriz[:, :-1]  # todas as colunas exceto a última
b = matriz[:, -1]   # somente a última coluna

if verificarDiagonalP(A):
    print("A matriz A é diagonalmente dominante.")
    solucao=gaussSeidel(A, b)
    print("Solução aproximada:", solucao)
else:
    resposta=input("A matriz A não é diagonalmente dominante. Deseja tentar a convergência mesmo assim? (s/n): ")
    if resposta.strip().lower()=='s':
        solucao=gaussSeidel(A, b)
        print("Solução aproximada:", solucao)
    else:
        print("Execução interrompida pelo usuário.")