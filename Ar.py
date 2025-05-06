#Qualidade do ar 

#PM10, PM2.5, NO2, SO2, CO

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


from Funcoes_Ar import gasPM10
from Funcoes_Ar import gasPM2_5
from Funcoes_Ar import gasNO2
from Funcoes_Ar import gasSO2
from Funcoes_Ar import gasCO


data = pd.read_csv('air_quality_dataset.csv')
print(data.columns)

data['Indice_PM10'] = data['PM10'].map(gasPM10)
data['Indice_PM2_5'] = data['PM2.5'].map(gasPM2_5)
data['Indice_NO2'] = data['NO2'].map(gasNO2)
data['Indice_SO2'] = data['SO2'].map(gasSO2)
data['Indice_CO'] = data['CO'].map(gasCO)

maiorIndicePorLocal = data.groupby('Location_Type')[['Indice_NO2', 'Indice_SO2', 'Indice_PM10', 'Indice_PM2_5', 'Indice_CO']].mean()
maiorIndicePorLocal.plot(kind='barh', figsize = (14,10), color=['green', 'purple', 'blue', 'yellow', 'black'])
plt.show()

print(data[['Location_Type','Indice_PM10', 'Indice_PM2_5', 'Indice_NO2', 'Indice_SO2', 'Indice_CO']])
    

