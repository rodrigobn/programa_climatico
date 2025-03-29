# Programa Climático

Este projeto é uma aplicação para análise de dados climáticos, permitindo a visualização e análise de informações como precipitação, temperatura mínima e máxima, umidade e vento a partir de um conjunto de dados em formato CSV.

## Estrutura do Projeto

```
programa_climatico
├── data
│   └── dados.csv          # Dados climáticos em formato CSV
├── src
│   ├── __init__.py        # Pacote Python para o diretório src
│   ├── main.py            # Ponto de entrada do programa
│   ├── utils              # Módulos de utilidades
│   │   ├── __init__.py    # Pacote Python para o diretório utils
│   │   ├── carregamento.py # Módulo para carregar dados climáticos
│   │   ├── visualizacao.py # Módulo para visualizar dados climáticos
│   │   ├── analise.py     # Módulo para análise de dados climáticos
│   │   └── graficos.py     # Módulo para geração de gráficos
├── requirements.txt       # Arquivo com as dependências do projeto
└── README.md              # Documentação do projeto
```

## Instalação

Para executar este projeto, você precisará ter o Python instalado em sua máquina. Você pode instalar as dependências necessárias usando o seguinte comando:

```
pip install -r requirements.txt
```

### Dependências

As dependências do projeto estão listadas no arquivo `requirements.txt`. A biblioteca utilizada é:

- `matplotlib`: Para geração de gráficos.

## Uso

Para executar o programa, você pode usar o seguinte comando:

```
python src/main.py
```

Siga as instruções exibidas no terminal para interagir com o programa.

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir um problema ou enviar um pull request.