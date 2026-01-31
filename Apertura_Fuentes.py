import pandas as pd
import numpy as ny
import openpyxl as opp
import requests

Ruta_excel = r"C:\Users\Randu\Desktop\Python\01 - BD CURSOS.xlsx"
Ruta_csv = r"C:\Users\Randu\Desktop\Python\Product_v6.csv"
URL_Cursos = "http://127.0.0.1:8000/cursos"
URL_Productos = "http://127.0.0.1:8000/productos"

def leer_archivos_locales(Ruta, Ruta2):
    try:
        excel = pd.read_excel(Ruta)
        csv = pd.read_csv(Ruta2)
        return excel, csv
    except FileNotFoundError:
        print("El archivo no existe")
        return None, None

def leer_API(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return pd.DataFrame(response.json())
    
    except requests.exceptions.RequestException as e:
        print(f"Error API: {e}")
        return None

#impresion de los datos df 
df_excel, df_csv = leer_archivos_locales(Ruta_excel, Ruta_csv)
df_api_cursos = leer_API(URL_Cursos)
df_api_productos = leer_API(URL_Productos)

print(df_excel.head(10))
print(df_csv.head(5))
print(df_api_cursos)
print(df_api_productos)

