import pandas as pd
from fuzzywuzzy import fuzz


ruta_archivo = r""


data = []

with open(ruta_archivo, 'r', encoding='utf-8') as file:
    for line in file:
   
        fields = line.strip().split(';')
        data.append(fields)

data_df = pd.DataFrame(data, columns=['Empresa'])


def calcular_similitud(nombre1, nombre2):
    return fuzz.token_sort_ratio(nombre1, nombre2)


resultados = []


for i, empresa_evaluada in enumerate(data_df['Empresa']):
  
    similitudes_empresa_evaluada = []
    

    for j, otra_empresa in enumerate(data_df['Empresa']):
        if i != j: 
            similitud = calcular_similitud(empresa_evaluada, otra_empresa)
            similitudes_empresa_evaluada.append({'Empresa evaluada': empresa_evaluada, 'Empresa similar': otra_empresa, 'Similitud': similitud})
    
  
    resultados.extend(similitudes_empresa_evaluada)

resultados_df = pd.DataFrame(resultados)

ruta_resultados = ruta_archivo.replace('.csv', '_resultados.csv')
resultados_df.to_csv(ruta_resultados, index=False)

print("Resultados guardados en:", ruta_resultados)
