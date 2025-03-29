import matplotlib.pyplot as plt

def plotar_grafico_temp_minima(medias, mes):
    """Gera um gráfico de barras com as médias de temperatura mínima."""
    if not medias:
        print("Nenhum dado disponível para gerar o gráfico.")
        return
    
    nome_mes = {
        1: 'Janeiro', 2: 'Fevereiro', 3: 'Março', 4: 'Abril',
        5: 'Maio', 6: 'Junho', 7: 'Julho', 8: 'Agosto',
        9: 'Setembro', 10: 'Outubro', 11: 'Novembro', 12: 'Dezembro'
    }[mes]
    
    anos = sorted(medias.keys())
    valores = [medias[ano] for ano in anos]
    
    plt.figure(figsize=(12, 6))
    bars = plt.bar(range(len(anos)), valores, color='skyblue')
    
    # Adicionar rótulos e título
    plt.title(f'Média de Temperatura Mínima - {nome_mes} ({min(anos)}-{max(anos)})', fontsize=14)
    plt.xlabel('Ano', fontsize=12)
    plt.ylabel('Temperatura Mínima Média (°C)', fontsize=12)
    plt.xticks(range(len(anos)), [str(ano) for ano in anos], rotation=45)
    
    # Adicionar valores nas barras
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2., height,
                 f'{height:.1f}',
                 ha='center', va='bottom')
    
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()