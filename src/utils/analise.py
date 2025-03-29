from collections import defaultdict

def mes_mais_chuvoso(dados):
    """Identifica o mês mais chuvoso no período disponível."""
    if not dados:
        print("Nenhum dado disponível para análise.")
        return
    
    precipitacao_por_mes = defaultdict(float)
    for d in dados:
        chave = f"{d['mes']:02d}/{d['ano']}"
        precipitacao_por_mes[chave] += d['precipitacao']
    
    if not precipitacao_por_mes:
        print("Nenhum dado de precipitação disponível.")
        return
    
    mes_chuvoso = max(precipitacao_por_mes.items(), key=lambda x: x[1])
    return mes_chuvoso

def calcular_medias_temp_minima(dados, mes):
    """Calcula as médias de temperatura mínima para um mês específico.
    
    Args:
        dados (list): Lista de dicionários com dados climáticos
        mes (int): Mês para o qual calcular as médias (1-12)
        
    Returns:
        dict: Dicionário com anos como chaves e médias como valores
    """
    if not dados:
        print("Nenhum dado disponível para análise.")
        return {}
    
    if not 1 <= mes <= 12:
        raise ValueError("Mês deve estar entre 1 e 12")
    
    medias = {}
    anos_disponiveis = sorted({d['ano'] for d in dados})
    
    for ano in anos_disponiveis:
        temps = [d['temp_min'] for d in dados if d['ano'] == ano and d['mes'] == mes]
        if temps:
            medias[ano] = sum(temps) / len(temps)
    
    return medias

def exibir_medias_temp_minima(medias, mes):
    """Exibe as médias de temperatura mínima calculadas."""
    if not medias:
        print(f"Não há dados disponíveis para o mês {mes}.")
        return
    
    nome_mes = {
        1: 'Janeiro', 2: 'Fevereiro', 3: 'Março', 4: 'Abril',
        5: 'Maio', 6: 'Junho', 7: 'Julho', 8: 'Agosto',
        9: 'Setembro', 10: 'Outubro', 11: 'Novembro', 12: 'Dezembro'
    }[mes]
    
    print(f"\nMédias de Temperatura Mínima - {nome_mes}")
    print("=" * 40)
    for ano, media in sorted(medias.items()):
        print(f"{ano}: {media:.1f}°C")

def calcular_media_geral_temp_minima(medias):
    """Calcula e exibe a média geral das temperaturas mínimas."""
    if not medias:
        print("Nenhum dado disponível para calcular a média geral.")
        return
    
    media_geral = sum(medias.values()) / len(medias)
    print(f"\nMédia geral da temperatura mínima: {media_geral:.2f}°C")