```markdown
# Iterative Methods for Linear Systems: Jacobi vs. Gauss-Seidel

Repositório contendo implementações em Python dos métodos iterativos de Jacobi e Gauss-Seidel para resolução de sistemas lineares.

## 📋 Descrição
Dois algoritmos numéricos para resolver sistemas lineares `Ax = b`:
- **Método de Jacobi**: Atualiza todas as variáveis simultaneamente usando valores da iteração anterior.
- **Método de Gauss-Seidel**: Atualiza variáveis sequencialmente usando valores já calculados na mesma iteração.

## ✨ Funcionalidades
- **Entrada Flexível**: 
  - Número de colunas detectado automaticamente
  - Aceita números inteiros ou decimais
- **Verificação de Convergência**:
  - Checagem automática de dominância diagonal
  - Opção para forçar execução
- **Parâmetros Customizáveis**:
  - Tolerância (`1e-10` padrão)
  - Máximo de iterações (`100` padrão)

## 📥 Requisitos
- Python 3.8+
- NumPy (`pip install numpy`)

## 🚀 Como Usar
1. **Entrada da Matriz**:
```bash
Número de linhas: 3
Linha 1: 4 2 1 8
Linha 2: 1 5 2 10
Linha 3: 1 2 6 12
```

2. **Execução**:
```bash
# Para Jacobi
python jacobi.py

# Para Gauss-Seidel
python gauss_seidel.py
```

## 📊 Comparação dos Métodos

| Característica              | Jacobi                     | Gauss-Seidel                |
|-----------------------------|----------------------------|-----------------------------|
| **Velocidade Convergência** | Mais lento                 | Mais rápido                 |
| **Uso de Memória**          | Mantém 2 vetores           | Atualiza vetor in-place     |
| **Complexidade**            | O(n²) por iteração         | O(n²) por iteração          |
| **Aplicação Ideal**         | Sistemas esparsos grandes  | Sistemas diagonal dominantes|

## 🧪 Exemplo Prático
**Sistema de Entrada**:
```
4x + 2y + z = 8
x + 5y + 2z = 10
x + 2y + 6z = 12
```

**Saída Gauss-Seidel**:
```
Convergiu após 15 iterações.
Solução aproximada: [1. 1. 2.]
```

**Saída Jacobi**:
```
Convergiu após 19 iterações.
Solução aproximada: [1. 1. 2.]
```

## ⚠️ Limitações
- Não trata singularidade da matriz
- Precisão limitada por ponto flutuante
- Performance degrada em sistemas mal condicionados
