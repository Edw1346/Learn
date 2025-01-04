import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

print("hecho")

df = pd.read_csv("Python\\gra.csv")

#grafico de lineas
sns.lineplot(data=df, x="mes", y="llamadas")

#grafico de barras
#sns.barplot(data=df, x="mes", y="llamadas")

#grafico de bigotes
#sns.boxplot(data=df, x="mes", y="llamadas")

#sns.regplot(data=df, x="mes", y="llamadas")



plt.plot("Junio", 6, "o")
plt.show()
