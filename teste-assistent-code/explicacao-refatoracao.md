# 🔍 Verificador de Números Primos

Um programa Python educativo que demonstra como verificar se um número é primo de forma eficiente.

---

## 📖 Descrição da Função

A função `eh_primo(numero)` verifica se um número inteiro é primo. Um **número primo** é um número maior que 1 que possui apenas dois divisores: 1 e ele mesmo.

### Assinatura
```python
def eh_primo(numero: int) -> bool
```

### Parâmetros
- **numero** (int): Um número inteiro a ser verificado

### Retorno
- **bool**: `True` se o número é primo, `False` caso contrário

### Exceções
- **TypeError**: Lançado se o argumento não for um número inteiro

---

## 🔬 Explicação Linha por Linha

### Linhas 1-11: Definição e Documentação

```python
def eh_primo(numero):
    """
    Verifica se um número é primo.
    
    Args:
        numero (int): Um número inteiro a ser verificado.
    
    Returns:
        bool: True se o número é primo, False caso contrário.
    """
```

- **`def eh_primo(numero):`** → Define uma função chamada `eh_primo` que recebe um parâmetro `numero`
- **Docstring** (texto entre `""" """`) → Documentação da função que explica:
  - O que a função faz
  - Qual tipo de dado ela espera (`Args`)
  - Qual tipo de dado ela retorna (`Returns`)

---

### Linhas 12-13: Validação de Entrada

```python
    if not isinstance(numero, int):
        raise TypeError("O argumento deve ser um número inteiro")
```

- **`isinstance(numero, int)`** → Verifica se `numero` é do tipo inteiro
- **`not`** → Inverte a condição: "se NÃO for inteiro"
- **`raise TypeError(...)`** → Gera um erro se o usuário passar um valor inválido
  - Exemplo: `eh_primo("5")` causaria erro com mensagem clara

---

### Linhas 15-16: Números Menores que 2

```python
    if numero < 2:
        return False
```

- Se o número for **menor que 2** (ex: 0, 1, -5), retorna `False`
- **Motivo:** Por definição, números primos começam do 2
- **`return`** encerra a função imediatamente

---

### Linhas 18-20: Caso Especial do Número 2

```python
    if numero == 2:
        return True
```

- Se o número **for exatamente 2**, retorna `True`
- **Motivo:** 2 é o **único número primo par** que existe!

---

### Linhas 22-24: Eliminação de Números Pares

```python
    if numero % 2 == 0:
        return False
```

- **`%`** → Operador módulo (resto da divisão)
- **`numero % 2 == 0`** → Verifica se o número é par
- Se for par (e não é 2), retorna `False`
- **Exemplos:**
  - `4 % 2 = 0` (par) → False
  - `5 % 2 = 1` (ímpar) → continua

---

### Linhas 26-28: Verificação Principal - O Coração do Algoritmo

```python
    for i in range(3, int(numero ** 0.5) + 1, 2):
        if numero % i == 0:
            return False
```

**Esta é a parte mais inteligente do código!**

#### Descomposição:

**`for i in range(3, int(numero ** 0.5) + 1, 2):`**

- **`for i in range(...)`** → Loop que itera (passa por) vários números
- **`range(inicio, fim, passo)`** → Gera sequência de números
  - **`3`** → Começa em 3 (já testamos 2 acima)
  - **`int(numero ** 0.5) + 1`** → Fim do intervalo
    - **`numero ** 0.5`** → Calcula a raiz quadrada
    - **`int(...)`** → Converte para inteiro
    - **`+ 1`** → Inclui este número
  - **`,  2`** → Passo de 2 (só números **ímpares**)

#### Por que até a raiz quadrada?

Se um número `n` tem um divisor maior que √n, então obrigatoriamente tem outro divisor menor que √n. Logo, só precisamos testar até √n!

**Exemplo:** √16 = 4, então se 16 tivesse um divisor > 4, teria um divisor < 4. Testando até 4 é suficiente!

#### Testando divisibilidade:

```python
    if numero % i == 0:
        return False
```

- Se `numero` é divisível por `i` (resto = 0), encontramos um divisor
- Portanto, **não é primo** → retorna `False` imediatamente

---

### Linha 30: Retorno Final

```python
    return True
```

- Se chegou aqui, testou **todos os divisores possíveis** e nenhum funciona
- Logo, o número **é primo!** Retorna `True`

---

### Linhas 34-45: Seção de Exemplo

```python
if __name__ == "__main__":
```

- **`if __name__ == "__main__":`** → Executa este bloco APENAS se o arquivo for executado diretamente
- Evita rodar exemplos se outro arquivo importar esta função

```python
    numeros_teste = [2, 3, 4, 5, 10, 13, 17, 20, 29, 100]
```

- **`[ ]`** → Sintaxe de lista em Python
- Cria uma lista com 10 números para testar

```python
    print("Verificação de números primos:")
    print("-" * 40)
```

- Imprime título e linha separadora
- **`"-" * 40`** → Repete o símbolo "-" 40 vezes

```python
    for num in numeros_teste:
        resultado = eh_primo(num)
        status = "é primo" if resultado else "não é primo"
        print(f"{num:3d} {status}")
```

- **`for num in numeros_teste:`** → Para cada número na lista
- **`resultado = eh_primo(num)`** → Chama a função
- **`... if ... else ...`** → Operador ternário (if/else em uma linha)
- **`f"{num:3d} {status}"`** → f-string formatada
  - `{num:3d}` → Imprime em 3 espaços, alinhado à direita

---

## 📚 Exemplos de Uso

### Uso Básico

```python
# Testando números individuais
print(eh_primo(7))      # True (7 é primo)
print(eh_primo(10))     # False (10 = 2 × 5)
print(eh_primo(13))     # True (13 é primo)
print(eh_primo(1))      # False (1 não é primo)
```

### Encontrando Primos em um Intervalo

```python
primos = [n for n in range(2, 20) if eh_primo(n)]
print(primos)  # [2, 3, 5, 7, 11, 13, 17, 19]
```

### Tratamento de Erros

```python
try:
    eh_primo("5")  # Erro!
except TypeError as e:
    print(f"Erro: {e}")  # Erro: O argumento deve ser um número inteiro
```

### Contando Primos até um Número

```python
def contar_primos(limite):
    return sum(1 for n in range(2, limite + 1) if eh_primo(n))

print(f"Há {contar_primos(100)} primos até 100")
# Há 25 primos até 100
```

---

## ⚡ Otimizações Utilizadas

| Otimização | Benefício |
|-----------|-----------|
| Verificar paridade separadamente | Elimina metade dos números imediatamente |
| Iterar apenas até √n | Reduz drasticamente as verificações |
| Iterar de 2 em 2 (só ímpares) | Pula números pares, mais eficiente |
| Validação de tipo no início | Evita erros durante a execução |

---

## 📊 Complexidade

- **Tempo:** O(√n) - onde n é o número sendo testado
- **Espaço:** O(1) - utiliza apenas variáveis constantes

---

## 🎯 Fluxograma do Algoritmo

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
