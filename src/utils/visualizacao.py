def visualizar_dados(dados):
    """Permite ao usuário visualizar dados climáticos em um intervalo específico.
    
    Args:
        dados (list): Lista de dicionários com os dados climáticos
        
    O usuário pode selecionar um intervalo de datas e o tipo de dados a visualizar.
    """
    if not dados:
        print("Nenhum dado disponível para visualização.")
        return
    
    anos = sorted({d['ano'] for d in dados})
    print(f"\nDados disponíveis de {min(anos)} a {max(anos)}")
    
    try:
        ano_inicio = int(input("Informe o ano inicial (ex: 2000): "))
        mes_inicio = int(input("Informe o mês inicial (1 a 12): "))
        ano_fim = int(input("Informe o ano final (ex: 2010): "))
        mes_fim = int(input("Informe o mês final (1 a 12): "))

        if not (1 <= mes_inicio <= 12 and 1 <= mes_fim <= 12):
            raise ValueError("Os meses devem estar entre 1 e 12.")
        
        if (ano_inicio, mes_inicio) > (ano_fim, mes_fim):
            raise ValueError("O período inicial deve ser anterior ao período final.")
            
        periodo_disponivel = any(
            (ano_inicio, mes_inicio) <= (d['ano'], d['mes']) <= (ano_fim, mes_fim)
            for d in dados
        )
        if not periodo_disponivel:
            raise ValueError("Não há dados disponíveis para o período informado.")

        print("\nEscolha o tipo de dados que deseja visualizar:")
        print("1 - Todos os dados")
        print("2 - Apenas precipitação")
        print("3 - Apenas temperatura (máxima e mínima)")
        print("4 - Apenas umidade e vento")
        
        tipo = input("Digite a opção desejada (1-4): ")
        if tipo not in ['1', '2', '3', '4']:
            raise ValueError("Opção inválida. Digite um número entre 1 e 4.")
        tipo = int(tipo)

        filtrados = [
            d for d in dados 
            if (ano_inicio, mes_inicio) <= (d['ano'], d['mes']) <= (ano_fim, mes_fim)
        ]

        colunas = {
            1: ['data', 'precipitacao', 'temp_max', 'temp_min', 'umidade', 'vento'],
            2: ['data', 'precipitacao'],
            3: ['data', 'temp_max', 'temp_min'],
            4: ['data', 'umidade', 'vento']
        }[tipo]

        cabecalho = {
            'data': 'Data',
            'precipitacao': 'Precipitação (mm)',
            'temp_max': 'Temp. Máx (°C)',
            'temp_min': 'Temp. Mín (°C)',
            'umidade': 'Umidade (%)',
            'vento': 'Vento (km/h)'
        }
        
        print("\n" + "=" * 80)
        print(f"DADOS CLIMÁTICOS - {mes_inicio}/{ano_inicio} a {mes_fim}/{ano_fim}")
        print("=" * 80)
        print("\t".join(cabecalho[col] for col in colunas))
        print("-" * 80)
        
        for item in filtrados:
            linha = []
            for col in colunas:
                if col == 'data':
                    linha.append(item[col])
                elif col in ['temp_max', 'temp_min']:
                    linha.append(f"{item[col]:.1f}°C")
                elif col == 'precipitacao':
                    linha.append(f"{item[col]:.1f}mm")
                elif col == 'umidade':
                    linha.append(f"{item[col]:.0f}%")
                elif col == 'vento':
                    linha.append(f"{item[col]:.1f}km/h")
            print("\t".join(linha))
            
    except ValueError as e:
        print(f"\nErro: {e}")