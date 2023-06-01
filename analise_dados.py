import pandas 
import plotly_express as px

#receber os dados da planilha, lidas pelo pandas
dados = pandas.read_excel("Teste.xlsx")

#listar primeiras linhas
dados.head(6)

#listar ultimas linhas
dados.tail()

#tamanho da tabela de dados
dados.shape

#tipo de dados
dados.dtypes

# gerando estatisticas 
dados.describe()

#visualização do gráfico
px.histogram(dados, x="Responsável", text_auto=True, color="Responsável")

#lista ordenada das colunas dentro da planilha
colunas = ['Responsável', 'Ocorrência', 'Data']

#mostragem do gracfico com a lista de ordenação feito na variavel (colunas)
for coluna in colunas:
    fig = px.histogram(dados, x=coluna, color="Ocorrência", text_auto=True)
    fig.write_html(f"Grafico de {coluna}.html")
    fig.show()

#outra lista ordenada para verificar outros dados a partir da coluna Usuário
lista_colunas = ["Usuário", "ET", "Data", "REQ"]
lista_colunas

#mostragem do gráfico a partir do responsavel
grafico = px.histogram(dados, x="Responsável", text_auto=True, color="Responsável")
grafico.show()
grafico.write_html("grafico_teste.html")