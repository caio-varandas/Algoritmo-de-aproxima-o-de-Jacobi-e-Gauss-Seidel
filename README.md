# Métodos Iterativos para Sistemas Lineares: Jacobi e Gauss-Seidel

Este repositório contém implementações dos métodos iterativos **Jacobi** e **Gauss-Seidel** para resolver sistemas de equações lineares. O método de Jacobi foi implementado em **C++**, enquanto o Gauss-Seidel foi desenvolvido em **Python**. Esses algoritmos são ideais para sistemas grandes e esparsos, onde métodos diretos (como eliminação gaussiana) são computacionalmente custosos.

---

## 📖 Visão Geral dos Algoritmos

### **Método de Jacobi (C++)**
- **Teoria**: 
  - Atualiza iterativamente cada variável usando os valores da iteração anterior.
  - Fórmula para a variável:

  - Exige que a matriz seja **diagonalmente dominante** para convergência garantida.
- **Implementação**:
  - Utiliza dois vetores para armazenar os valores das iterações atual e seguinte.
  - A convergência é verificada pela diferença absoluta máxima entre iterações (`tolerância`).
  - Estrutura de loop simples com atualizações explícitas elemento a elemento.

### **Método de Gauss-Seidel (Python)**
- **Teoria**:
  - Acelera a convergência usando os valores mais recentes atualizados **dentro da mesma iteração**.
  - Fórmula atualiza:

  - Também requer dominância diagonal para convergência.
- **Implementação**:
  - Utiliza a biblioteca `numpy` para operações eficientes com matrizes e vetores.
  - Atualiza o vetor solução **no mesmo vetor**, reduzindo o uso de memória.
  - Critério de parada baseado na norma do resíduo ou diferença entre iterações.

---

## 📊 Exemplo de Saída
Ambos os algoritmos exibem:
- A solução aproximada do sistema.
- O número de iterações realizadas.
- O erro final (diferença entre iterações ou norma do resíduo).

---

## 📌 Considerações
- **Convergência**: Ambos os métodos exigem que a matriz seja diagonalmente dominante ou positiva definida.
- **Desempenho**: Gauss-Seidel geralmente converge mais rápido que Jacobi devido à atualização em tempo real dos valores.
- **Aplicações**: Úteis em problemas de engenharia, física computacional e otimização onde sistemas grandes são comuns.
