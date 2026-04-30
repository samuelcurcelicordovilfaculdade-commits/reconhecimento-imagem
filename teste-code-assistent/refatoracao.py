from typing import NamedTuple, List


class EstatisticasNumericas(NamedTuple):
    """
    Estrutura de dados para armazenar estatísticas de uma sequência de números.
    
    Attributes:
        soma_total: Soma de todos os números
        media: Média aritmética dos números
        valor_maximo: Maior valor na sequência
        valor_minimo: Menor valor na sequência
    """
    soma_total: float
    media: float
    valor_maximo: float
    valor_minimo: float


def calcular_estatisticas_numericas(numeros: List[float]) -> EstatisticasNumericas:
    """
    Calcula estatísticas básicas de uma sequência de números.
    
    Realiza os seguintes cálculos:
    - Soma total de todos os valores
    - Média aritmética (soma / quantidade)
    - Valor máximo
    - Valor mínimo
    
    Args:
        numeros: Lista de números (float ou int) para análise.
    
    Returns:
        EstatisticasNumericas: NamedTuple contendo:
            - soma_total: Resultado da soma
            - media: Valor médio
            - valor_maximo: Maior valor encontrado
            - valor_minimo: Menor valor encontrado
    
    Raises:
        ValueError: Se a lista estiver vazia.
        TypeError: Se a lista contiver valores não numéricos.
    
    Examples:
        >>> resultado = calcular_estatisticas_numericas([10, 20, 30])
        >>> resultado.media
        20.0
        >>> resultado.valor_maximo
        30
    """
    if not numeros:
        raise ValueError("A lista de números não pode estar vazia")
    
    # Calcula a soma total
    soma_total = sum(numeros)
    
    # Calcula a média aritmética
    media = soma_total / len(numeros)
    
    # Encontra o valor máximo e mínimo
    valor_maximo = max(numeros)
    valor_minimo = min(numeros)
    
    return EstatisticasNumericas(
        soma_total=soma_total,
        media=media,
        valor_maximo=valor_maximo,
        valor_minimo=valor_minimo
    )


def exibir_estatisticas(resultado: EstatisticasNumericas) -> None:
    """
    Exibe as estatísticas de forma formatada.
    
    Args:
        resultado: NamedTuple contendo as estatísticas a exibir.
    """
    print(f"Total:    {resultado.soma_total}")
    print(f"Média:    {resultado.media:.2f}")
    print(f"Máximo:   {resultado.valor_maximo}")
    print(f"Mínimo:   {resultado.valor_minimo}")


if __name__ == "__main__":
    # Lista de números para análise
    numeros_para_analisar = [23, 7, 45, 2, 67, 12, 89, 34, 56, 11]
    
    # Calcula as estatísticas
    resultado_estatisticas = calcular_estatisticas_numericas(numeros_para_analisar)
    
    # Exibe os resultados
    print("Estatísticas dos números:")
    print("-" * 40)
    exibir_estatisticas(resultado_estatisticas)
    
    # Exemplo de acesso aos dados individuais
    print("\n" + "-" * 40)
    print(f"Acessando dados individuais:")
    print(f"  Soma total via atributo: {resultado_estatisticas.soma_total}")
    print(f"  Soma total via índice: {resultado_estatisticas[0]}")