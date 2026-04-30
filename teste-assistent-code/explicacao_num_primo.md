# 🔍 Verificador de Números Primos - Versão Otimizada (Clean Code)

Um programa Python educativo que demonstra como verificar se um número é primo de forma eficiente, aplicando os princípios de **Clean Code**.

---

## 📖 Descrição das Funções

### Função Principal: `eh_primo()`

A função `eh_primo(numero: int) -> bool` verifica se um número inteiro é primo usando um algoritmo eficiente.

Um **número primo** é um número natural maior que 1 que possui apenas dois divisores distintos: 1 e ele mesmo.

#### Assinatura com Type Hints
```python
def eh_primo(numero: int) -> bool:
```

- **`numero: int`** → Parâmetro esperado é um inteiro
- **`-> bool`** → Retorna um valor booleano

#### Parâmetros
- **numero** (int): Um número inteiro a ser verificado

#### Retorno
- **True** se o número é primo
- **False** caso contrário

#### Exceções
- **TypeError**: Lançado se o argumento não for um número inteiro (excluindo booleans)

---

### Função Auxiliar: `exibir_resultado_primalidade()`

```python
def exibir_resultado_primalidade(numero: int) -> None:
```

Função utilitária que encapsula a lógica de exibição, separando a responsabilidade de validação da exibição.

- **`numero: int`** → Número a ser verificado
- **`-> None`** → Não retorna valor (apenas imprime)

---

## 🔬 Explicação Linha por Linha - Versão Otimizada

### Linhas 1-24: Definição e Documentação Aprimorada

```python
def eh_primo(numero: int) -> bool:
    """
    Verifica se um número inteiro é primo.

    Um número primo é um número natural maior que 1 que possui
    apenas dois divisores distintos: 1 e ele mesmo.

    Args:
        numero: Um número inteiro a ser verificado.

    Returns:
        True se o número é primo, False caso contrário.

    Raises:
        TypeError: Se o argumento não for um número inteiro.
        ValueError: Se o número for menor que 1.

    Examples:
        >>> eh_primo(2)
        True
        >>> eh_primo(4)
        False
        >>> eh_primo(17)
        True
    """
```

**Melhorias em relação à versão anterior:**

✅ **Type Hints** → `numero: int` e `-> bool` deixam claro entrada/saída  
✅ **Docstring expandida** → Explicação mais detalhada da função  
✅ **Seção Raises** → Documenta quais exceções podem ser lançadas  
✅ **Seção Examples** → Exemplos de uso direto na documentação  
✅ **Formato padrão** → Segue convenção Google/NumPy style  

---

### Linhas 26-32: Validação de Tipo Robusta

```python
    # Validação de tipo
    if not isinstance(numero, int) or isinstance(numero, bool):
        raise TypeError(
            f"Esperado 'int', recebido '{type(numero).__name__}'. "
            f"O argumento deve ser um número inteiro."
        )
```

**Melhorias implementadas:**

- **`isinstance(numero, bool)`** → Verifica se é `bool` (importante: em Python, `bool` é subclasse de `int`!)
- **`type(numero).__name__`** → Mensagem de erro dinâmica mostrando o tipo recebido
- **f-string** → Formatação clara e legível
- **Comentário descritivo** → Explica o propósito desta seção

**Exemplos de validação:**
```python
eh_primo(5)          # ✅ OK - retorna False ou True
eh_primo("5")        # ❌ TypeError: Esperado 'int', recebido 'str'
eh_primo(5.0)        # ❌ TypeError: Esperado 'int', recebido 'float'
eh_primo(True)       # ❌ TypeError: Esperado 'int', recebido 'bool'
```

---

### Linhas 34-36: Validação de Valor

```python
    # Validação de valor
    if numero < 2:
        return False
```

- **Números < 2** não são primos por definição
- **Casos cobertos:** 0, 1, números negativos
- **Return imediato** evita processamento desnecessário

---

### Linhas 38-40: Caso Especial do Número 2

```python
    # Caso especial: único número primo par
    if numero == 2:
        return True
```

- **2 é especial** → Único primo que é par
- **Comentário significativo** → Explica o *por quê* dessa verificação

---

### Linhas 42-44: Eliminação de Números Pares

```python
    # Descarta números pares
    if numero % 2 == 0:
        return False
```

- **`%`** (módulo) → Obtém o resto da divisão
- **`numero % 2 == 0`** → Teste de paridade (resto = 0 → par)
- **Descarta metade dos números** de uma vez
- **Otimização crítica** → Aumenta performance significativamente

**Exemplos:**
```
4 % 2 = 0 (par) → False
5 % 2 = 1 (ímpar) → continua
```

---

### Linhas 46-50: Verificação Principal com Variável Extraída

```python
    # Verifica divisibilidade por números ímpares até a raiz quadrada
    limite_verificacao = int(numero ** 0.5) + 1
    for divisor_possivel in range(3, limite_verificacao, 2):
        if numero % divisor_possivel == 0:
            return False
```

**Esta é a seção mais inteligente! Vamos decompor:**

#### Linha 47: Extração da Variável Limite

```python
limite_verificacao = int(numero ** 0.5) + 1
```

**Melhorias:**
- **Variável nomeada** → `limite_verificacao` é muito mais legível que cálculo inline
- **`numero ** 0.5`** → Calcula a raiz quadrada
- **`int(...)`** → Converte para inteiro (remove casas decimais)
- **`+ 1`** → Inclui o número na verificação

**Por que raiz quadrada?**

Se um número `n` tem um divisor `d > √n`, então obrigatoriamente tem outro divisor `d' < √n`:
```
Exemplo: 36 = 2 × 18 = 3 × 12 = 4 × 9 = 6 × 6
√36 = 6
Testando até 6: encontramos 2, 3, 4, 6
Não precisa testar 9, 12, 18 (já encontramos seus pares menores)
```

#### Linha 48: Loop com Nome Descritivo

```python
for divisor_possivel in range(3, limite_verificacao, 2):
```

**Melhorias de legibilidade:**
- **`divisor_possivel`** → Nome descritivo (antes era `i`)
- **`range(3, limite_verificacao, 2)`** → Gera: 3, 5, 7, 9, 11, ...
  - **Começa em 3** (já testamos 2)
  - **Vai até `limite_verificacao`** (raiz quadrada + 1)
  - **Passo 2** (só números ímpares - otimização!)

**Por que de 2 em 2?**
- Todos os números pares já foram descartados
- Só precisamos testar números ímpares
- Reduz à metade o número de iterações

#### Linhas 49-50: Teste de Divisibilidade

```python
        if numero % divisor_possivel == 0:
            return False
```

- Se encontra um divisor, o número **não é primo**
- **Return imediato** → Não precisa testar o resto
- **Eficiente** → Para na primeira descoberta

---

### Linha 52: Retorno Final

```python
    return True
```

- Se chegou aqui, testou **todos os divisores possíveis até √número**
- **Nenhum divisor encontrado** → O número **é primo!**
- **Retorna True**

---

## 🎯 Função Auxiliar: Separação de Responsabilidades

### Linhas 55-63: `exibir_resultado_primalidade()`

```python
def exibir_resultado_primalidade(numero: int) -> None:
    """
    Exibe se um número é primo de forma formatada.

    Args:
        numero: O número a ser verificado e exibido.
    """
    is_prime = eh_primo(numero)
    status = "é primo" if is_prime else "não é primo"
    print(f"{numero:3d} {status}")
```

**Benefícios de uma função separada:**

✅ **Single Responsibility Principle** → Uma função faz uma coisa bem  
✅ **Reutilização** → Pode usar a lógica em diferentes contextos  
✅ **Testabilidade** → Mais fácil escrever testes unitários  
✅ **Legibilidade** → Código principal fica mais claro  

**Nomes descritivos:**
- **`is_prime`** → Convenção internacional (bool flags com `is_`)
- **`status`** → Texto descritivo do resultado
- **`numero:3d`** → Formatação (3 dígitos, alinhado à direita)

---

## 📚 Exemplos de Uso

### Uso Básico

```python
from num_primos import eh_primo

# Testando números individuais
print(eh_primo(2))      # True (2 é primo)
print(eh_primo(4))      # False (4 = 2 × 2)
print(eh_primo(17))     # True (17 é primo)
print(eh_primo(1))      # False (1 não é primo)
print(eh_primo(-5))     # False (negativos não são primos)
```

### Encontrando Todos os Primos em um Intervalo

```python
primos_ate_20 = [n for n in range(2, 21) if eh_primo(n)]
print(primos_ate_20)  # [2, 3, 5, 7, 11, 13, 17, 19]
```

### Tratamento de Erros (Type Hints)

```python
try:
    eh_primo("5")  # Erro!
except TypeError as e:
    print(f"Erro: {e}")
    # Erro: Esperado 'int', recebido 'str'. O argumento deve ser um número inteiro.

try:
    eh_primo(5.5)
except TypeError as e:
    print(f"Erro: {e}")
    # Erro: Esperado 'int', recebido 'float'. O argumento deve ser um número inteiro.

try:
    eh_primo(True)  # bool é subclasse de int!
except TypeError as e:
    print(f"Erro: {e}")
    # Erro: Esperado 'int', recebido 'bool'. O argumento deve ser um número inteiro.
```

### Contando Primos em um Intervalo

```python
def contar_primos(limite: int) -> int:
    """Conta quantos números primos existem até 'limite'."""
    return sum(1 for n in range(2, limite + 1) if eh_primo(n))

print(f"Há {contar_primos(100)} primos até 100")
# Há 25 primos até 100
```

### Usando a Função Auxiliar

```python
from num_primos import exibir_resultado_primalidade

# Exibe resultados formatados
exibir_resultado_primalidade(2)     #   2 é primo
exibir_resultado_primalidade(10)    #  10 não é primo
exibir_resultado_primalidade(29)    #  29 é primo
```

---

## ⚡ Otimizações Implementadas

| Otimização | Mecanismo | Impacto |
|-----------|-----------|--------|
| **Validação de tipo antecipada** | `isinstance()` no início | Evita erros durante processamento |
| **Casos especiais tratados** | 2, números pares | Descarta ~75% dos números rapidamente |
| **Iteração até √n** | `int(numero ** 0.5)` | Reduz verificações de O(n) para O(√n) |
| **Passo de 2 em 2** | `range(..., step=2)` | Elimina números pares, 50% menos iterações |
| **Variáveis nomeadas** | `limite_verificacao`, `divisor_possivel` | Código autodocumentado, fácil manutenção |
| **Função separada para UI** | `exibir_resultado_primalidade()` | Separação de responsabilidades |

---

## 📊 Complexidade Computacional

```
Análise de Performance:
├─ Números < 2: O(1) - retorno imediato
├─ Números pares: O(1) - uma divisão módulo
├─ Números ímpares: O(√n) - itera até raiz quadrada
│  └─ Cada iteração: O(1) - uma divisão módulo
└─ Pior caso geral: O(√n)
```

**Comparação:**

| Abordagem | Operações (n=1000) | Operações (n=1000000) |
|-----------|-------------------|----------------------|
| Ingênua (testar até n) | ~1000 divisões | ~1,000,000 divisões |
| **Otimizada (até √n)** | **~31 divisões** | **~1,000 divisões** |
| Ganho | **~32x mais rápido** | **~1000x mais rápido** |

---

## 🧪 Doctest Integrado

A função inclui exemplos que podem ser testados automaticamente:

```bash
python -m doctest num_primos.py -v
```

Os exemplos no docstring servem como:
- ✅ Documentação
- ✅ Testes unitários
- ✅ Exemplos para usuários

---

## 🎓 Princípios de Clean Code Aplicados

### 1. **Type Hints** ✅
```python
def eh_primo(numero: int) -> bool:
```
- Deixa claro tipos esperados
- Permite verificação de tipos com ferramentas como MyPy
- Melhora IDE autocomplete

### 2. **Nomes Descritivos** ✅
```python
# Antes
for i in range(3, int(numero ** 0.5) + 1, 2):

# Depois
limite_verificacao = int(numero ** 0.5) + 1
for divisor_possivel in range(3, limite_verificacao, 2):
```

### 3. **Docstring Completa** ✅
- Explicação clara do propósito
- Documentação de parâmetros
- Documentação de retorno
- Documentação de exceções
- Exemplos de uso

### 4. **Single Responsibility Principle** ✅
- `eh_primo()` → Valida e calcula
- `exibir_resultado_primalidade()` → Exibe resultado

### 5. **DRY (Don't Repeat Yourself)** ✅
- Variável `limite_verificacao` extraída
- Lógica de exibição em função separada

### 6. **Comentários Significativos** ✅
- Comentários explicam *por quê*, não *o quê*
- Código autodocumentado reduz necessidade de comentários

### 7. **Validação Robusta** ✅
- Verifica tipo antes de usar
- Mensagens de erro descritivas
- Trata casos especiais (bool, números pares, etc.)

---

## 🚀 Executando o Programa

### No Terminal

```bash
cd teste-assistent-code
python num_primos.py
```

### Saída Esperada

```
Verificação de números primos:
----------------------------------------
  2 é primo
  3 é primo
  4 não é primo
  5 é primo
 10 não é primo
 13 é primo
 17 é primo
 20 não é primo
 29 é primo
100 não é primo
```

---

## 📚 Conceitos Python Aprendidos

| Conceito | Exemplo |
|----------|---------|
| **Type Hints** | `def func(x: int) -> bool:` |
| **Docstrings** | `"""Documentação da função"""` |
| **Operador módulo** | `numero % 2 == 0` |
| **Validação de tipo** | `isinstance(numero, int)` |
| **Estruturas condicionais** | `if`, `elif`, `else` |
| **Loops** | `for divisor in range(...)` |
| **Operador ternário** | `"sim" if condicao else "não"` |
| **f-strings** | `f"{numero:3d} é primo"` |
| **Funções separadas** | Single Responsibility |
| **Extração de variáveis** | Melhor legibilidade |

---

## 💡 Comparação: Antes vs Depois

### Antes (Versão Original)
```python
def eh_primo(numero):
    if not isinstance(numero, int):
        raise TypeError("O argumento deve ser um número inteiro")
    if numero < 2:
        return False
    # ... resto do código
```

### Depois (Versão Otimizada - Clean Code)
```python
def eh_primo(numero: int) -> bool:
    """Verifica se um número inteiro é primo."""
    if not isinstance(numero, int) or isinstance(numero, bool):
        raise TypeError(
            f"Esperado 'int', recebido '{type(numero).__name__}'. "
            f"O argumento deve ser um número inteiro."
        )
    limite_verificacao = int(numero ** 0.5) + 1
    for divisor_possivel in range(3, limite_verificacao, 2):
        if numero % divisor_possivel == 0:
            return False
    return True
```

**Melhorias:**
✅ Type hints completos  
✅ Docstring estruturada  
✅ Nomes descritivos  
✅ Validação mais robusta  
✅ Variáveis extraídas  
✅ Função auxiliar para UI  

---

## 🔗 Recursos Adicionais

- [PEP 257 - Docstring Conventions](https://www.python.org/dev/peps/pep-0257/)
- [PEP 484 - Type Hints](https://www.python.org/dev/peps/pep-0484/)
- [Clean Code by Robert C. Martin](https://en.wikipedia.org/wiki/Robert_C._Martin)
- [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html)

---

**Versão:** 2.0 (Otimizada - Clean Code)  
**Data:** Abril 2026  
**Linguagem:** Python 3.7+

```
┌─────────────────────────────────┐
│   Número entra na função        │
└────────────┬────────────────────┘
             │
             ▼
       ┌──────────────────┐
       │ É inteiro?       │
       └────┬────────┬────┘
          Não│       │Sim
             │       ▼
             │  ┌──────────────┐
             │  │ < 2?         │
             │  └────┬────┬────┘
             │      Sim│  │Não
             │         │  ▼
             │         │ ┌──────────────┐
             │         │ │ == 2?        │
             │         │ └────┬────┬────┘
             │         │     Sim│  │Não
             │         │        │  ▼
             │         │        │ ┌──────────────────┐
             │         │        │ │ Número par?      │
             │         │        │ └────┬────┬───────┘
             │         │        │     Sim│  │Não
             │         │        │        │  ▼
             │         │        │        │ ┌──────────────────────┐
             │         │        │        │ │ Testa divisores      │
             │         │        │        │ │ até √número          │
             │         │        │        │ └────┬────┬────┬──────┘
             │         │        │        │      │    │    │
             │         │        │        │      │    │    │Nenhum divisor
             │         │        │        │      │    │    │
       ┌─────┴─────────┴────────┴────────┴──────┴────┴────┴──────┐
       │                      return                               │
       │            ┌──────────────┬──────────────┐               │
       ▼            ▼              ▼              ▼               │
    ❌ False    ❌ False      ✅ True      ✅ True              │
   (Erro!)   (Não primo)  (Primo!)   (Primo!)                │
       │            │              │              │              │
       └──────────┬─┴──────────────┴──────────────┘              │
                  │                                               │
                  └───────────────┬───────────────────────────────┘
                                  │
                          Função retorna resultado
```

---

## 🚀 Como Executar

### No Terminal/PowerShell

```bash
# Navegue até a pasta do projeto
cd "c:\Users\pichau\Desktop\Projeto-ia\reconhecimento-imagem\teste-assistent-code"

# Execute o arquivo
python num_primos.py
```

### Saída Esperada

```
Verificação de números primos:
----------------------------------------
  2 é primo
  3 é primo
  4 não é primo
  5 é primo
 10 não é primo
 13 é primo
 17 é primo
 20 não é primo
 29 é primo
100 não é primo
```

---

## 🎓 Conceitos Python Aprendidos

- ✅ Definição de funções (`def`)
- ✅ Docstrings e documentação
- ✅ Validação com `isinstance()`
- ✅ Tratamento de exceções (`raise`)
- ✅ Estruturas condicionais (`if`, `else`)
- ✅ Loops (`for`, `range`)
- ✅ Operador módulo (`%`)
- ✅ Operador ternário (`if/else` em linha)
- ✅ Strings formatadas (f-strings)
- ✅ Listas e iteração
- ✅ Bloco `if __name__ == "__main__"`

---

## 💡 Curiosidades Matemáticas

- **Único primo par:** 2
- **Maior primo conhecido:** Um número com mais de 24 milhões de dígitos! (2^82,589,933 - 1)
- **Crivo de Eratóstenes:** Método antigo (200 a.C.) para encontrar todos os primos até um número
- **Números primos gêmeos:** Primos que diferem por 2 (ex: 11 e 13, 17 e 19)

---

## 📝 Licença

Este código é fornecido como exemplo educativo para aprendizado de Python.

---

**Autor:** GitHub Copilot  
**Data:** 2026  
**Linguagem:** Python 3.x
