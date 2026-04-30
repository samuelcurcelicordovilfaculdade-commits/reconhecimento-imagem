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
    # Validação de tipo
    if not isinstance(numero, int) or isinstance(numero, bool):
        raise TypeError(
            f"Esperado 'int', recebido '{type(numero).__name__}'. "
            f"O argumento deve ser um número inteiro."
        )

    # Validação de valor
    if numero < 2:
        return False

    # Caso especial: único número primo par
    if numero == 2:
        return True

    # Descarta números pares
    if numero % 2 == 0:
        return False

    # Verifica divisibilidade por números ímpares até a raiz quadrada
    limite_verificacao = int(numero ** 0.5) + 1
    for divisor_possivel in range(3, limite_verificacao, 2):
        if numero % divisor_possivel == 0:
            return False

    return True


def exibir_resultado_primalidade(numero: int) -> None:
    """
    Exibe se um número é primo de forma formatada.

    Args:
        numero: O número a ser verificado e exibido.
    """
    is_prime = eh_primo(numero)
    status = "é primo" if is_prime else "não é primo"
    print(f"{numero:3d} {status}")


if __name__ == "__main__":
    # Lista de números para teste
    numeros_para_testar = [2, 3, 4, 5, 10, 13, 17, 20, 29, 100]

    print("Verificação de números primos:")
    print("-" * 40)

    for numero in numeros_para_testar:
        exibir_resultado_primalidade(numero)
