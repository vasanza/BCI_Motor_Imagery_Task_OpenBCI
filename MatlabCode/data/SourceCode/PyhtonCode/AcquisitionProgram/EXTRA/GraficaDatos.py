import pandas as pd
import matplotlib.pyplot as plt

libro="Recoleccion/S26M_.csv"
df=pd.read_csv(libro)
data=df["1"]

print(data.head())
plt.figure()
data.plot()
plt.show()
