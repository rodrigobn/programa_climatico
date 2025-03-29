import csv

def carregar_dados(arquivo):
    """Carrega os dados climáticos de um arquivo CSV.
    
    Args:
        arquivo (str): Caminho para o arquivo CSV contendo os dados climáticos
        
    Returns:
        list: Lista de dicionários com os dados formatados e validados
        
    Raises:
        FileNotFoundError: Se o arquivo não for encontrado
        ValueError: Se houver erro na formatação dos dados
    """
    dados = []
    try:
        with open(arquivo, newline='', encoding='utf-8') as f:
            leitor = csv.DictReader(f)
            for linha_num, linha in enumerate(leitor, 1):
                try:
                    # Validação da data
                    data = linha['data']
                    try:
                        dia, mes, ano = map(int, data.split('/'))
                        if not (1 <= mes <= 12):
                            raise ValueError("Mês inválido")
                    except (ValueError, IndexError):
                        raise ValueError(f"Formato de data inválido: {data}")
                    
                    # Validação dos valores numéricos
                    precipitacao = float(linha['precip'])
                    temp_max = float(linha['maxima'])
                    temp_min = float(linha['minima'])
                    umidade = float(linha['um_relativa'])
                    vento = float(linha['vel_vento'])
                    
                    # Validação de valores plausíveis
                    if temp_min > temp_max:
                        raise ValueError("Temperatura mínima maior que máxima")
                    if not (0 <= umidade <= 100):
                        raise ValueError("Umidade relativa fora do intervalo 0-100%")
                    
                    dados.append({
                        'data': data,
                        'ano': ano,
                        'mes': mes,
                        'dia': dia,
                        'precipitacao': precipitacao,
                        'temp_max': temp_max,
                        'temp_min': temp_min,
                        'umidade': umidade,
                        'vento': vento
                    })
                    
                except (ValueError, KeyError) as e:
                    print(f"Erro na linha {linha_num}: {e}. Linha ignorada.")
                    continue
                    
    except FileNotFoundError:
        print(f"Erro: Arquivo '{arquivo}' não encontrado.")
        return None
        
    return dados