from utils.carregamento import carregar_dados
from utils.visualizacao import visualizar_dados
from utils.analise import mes_mais_chuvoso, calcular_medias_temp_minima, exibir_medias_temp_minima, calcular_media_geral_temp_minima, calcular_medias_temp_minima_2006_2016
from utils.graficos import plotar_grafico_temp_minima


def exibir_separador(titulo=""):
    """ Função para exibir um separador com título """
    print("\n" + "=" * 50)
    if titulo:
        print(titulo.center(50))
        print("=" * 50)


def menu_principal():
    """ Função para exibir o menu principal e capturar a opção do usuário """
    print("\n" + "=" * 50)
    print("ANÁLISE DE DADOS CLIMÁTICOS".center(50))
    print("=" * 50)
    print("1. Visualizar dados em intervalo específico")
    print("2. Identificar mês mais chuvoso")
    print("3. Analisar temperaturas mínimas de um mês")
    print("4. Sair")
    
    while True:
        opcao = input("\nDigite a opção desejada (1-4): ")
        if opcao in ['1', '2', '3', '4']:
            return int(opcao)
        print("Erro: Opção inválida. Digite um número entre 1 e 4.")


def main():
    arquivo = 'data/dados.csv'
    dados = carregar_dados(arquivo)
    if not dados:
        exibir_separador("Erro")
        print("Não foi possível carregar os dados. Verifique o arquivo.")
        return
    
    while True:
        opcao = menu_principal()
        
        if opcao == 1:
            exibir_separador("Visualização de Dados")
            visualizar_dados(dados)
            exibir_separador("Fim da Visualização")
        elif opcao == 2:
            exibir_separador("Mês Mais Chuvoso")
            resultado = mes_mais_chuvoso(dados)
            if resultado:
                mes, precipitacao = resultado
                print(f"O mês mais chuvoso foi {mes} com {precipitacao:.2f} mm de precipitação.")
            else:
                print("Não foi possível determinar o mês mais chuvoso.")
            exibir_separador("Fim da Análise")
        elif opcao == 3:
            exibir_separador("Análise de Temperaturas Mínimas")
            try:
                mes = int(input("Digite o mês para análise (1-12): "))
                if not 1 <= mes <= 12:
                    print("Erro: Mês deve estar entre 1 e 12.")
                    continue
                    
                medias = calcular_medias_temp_minima_2006_2016(dados, mes)
                if medias:
                    print("\nMédias de Temperatura Mínima (2006-2016):")
                    for chave, media in medias.items():
                        print(f"{chave}: {media:.2f}°C")
                    
                    # Geração do gráfico
                    plotar_grafico_temp_minima(medias, mes)
                    
                    # Cálculo da média geral
                    calcular_media_geral_temp_minima(medias)
                else:
                    print("Não há dados disponíveis para o período informado.")
            except ValueError:
                print("Erro: Digite um número válido para o mês.")
            exibir_separador("Fim da Análise")
        elif opcao == 4:
            exibir_separador("Encerrando o Programa")
            print("Obrigado por usar o programa!")
            break

if __name__ == "__main__":
    main()