import plotly.graph_objs as go
import plotly.offline as pyo

# Dados fictícios
labels = ['Bicicleta ', 'Tênis de corrida', 'Skate de Rua', 'Bola de Futebol', 'Raquete de Tênis']
values = [15, 30, 25, 10, 20]

# Criação do gráfico em pizza
data = [go.Pie(labels=labels, values=values)]

# Criação do layout do gráfico
layout = go.Layout(title='Vendas de produtos esportivos do mês')

# Criação da figura do gráfico
fig = go.Figure(data=data, layout=layout)

# Renderização do gráfico em um arquivo HTML
pyo.plot(fig, filename='dashboard_pizza.html')