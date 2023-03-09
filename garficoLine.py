#importando a biblioteca
import matplotlib.pyplot as plt

#listas 
meses = ["Janeiro","Fevereiro","Março","Abril","Maio","Junho"]
valores = [105235, 107697, 110256, 109236, 108859, 109986]

#variaveis legendas
titulo = "Dados da Venda"
m = "\n Meses"
v = "Valores\n"

#legendas
plt.title(titulo, color="green")
plt.xlabel(m, color="blue")
plt.ylabel(v, color="red")

#visualização
plt.plot(meses, valores, label="Pontos" ,color="#9932CC", marker=".", linestyle="-")
plt.scatter(meses, valores )
plt.show()