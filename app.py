import pandas as pd
import requests


def extract_data_from_url() -> pd.DataFrame:
    url = "https://www.datos.gov.co/resource/9mey-c8s8.json"
    response = requests.get(url)
    response.raise_for_status() 
    data = response.json()
    return pd.DataFrame(data)

#Tranformar
def transform_data(df: pd.DataFrame) -> pd.DataFrame:
    
    if 'cobertuta_4g' in df.columns:
        df['cobertura_4g'] = df.pop('cobertuta_4g')

    # Columnas convertir de 'S'/'N' a 'SI'/'NO'
    cobertura_cols = [
        'cabecera_municipal',
        'cobertura_2g',
        'cobertura_3g',
        'cobertura_hspa_hspa_dc',
        'cobertura_4g',
        'cobertura_lte',
        'cobertura_5g'
    ]

    for col in cobertura_cols:
        if col in df.columns:
            df[col] = df[col].map({'S': 1, 'N': 0}).fillna(df[col])

    # Renombrar columnas
    df.rename(columns={
        'a_o': 'AÑO',
        'trimestre': 'TRIMESTRE',
        'proveedor': 'PROVEEDOR',
        'cod_departamento': 'COD DEPARTAMENTO',
        'departamento': 'DEPARTAMENTO',
        'cod_municipio': 'COD MUNICIPIO',
        'municipio': 'MUNICIPIO',
        'cabecera_municipal': 'CABECERA MUNICIPAL',
        'cod_centro_poblado': 'COD CENTRO POBLADO',
        'centro_poblado': 'CENTRO POBLADO',
        'cobertura_2g': 'COBERTURA 2G',
        'cobertura_3g': 'COBERTURA 3G',
        'cobertura_hspa_hspa_dc': 'COBERTURA HSPA+, HSPA+DC',
        'cobertura_4g': 'COBERTURA 4G',
        'cobertura_lte': 'COBERTURA LTE',
        'cobertura_5g': 'COBERTURA 5G'
    }, inplace=True)

    
    return df


def load_to_csv(df: pd.DataFrame, filename: str):
    df.to_csv(filename, index=False, encoding='utf-8-sig')


def run_etl():
    df = extract_data_from_url()
    df_clean = transform_data(df)
    print(df_clean.head())  # Mostrar datos ya transformados
    load_to_csv(df_clean, "cobertura_movil_transformado.csv")
    print("Archivo generado: cobertura_movil_transformado.csv")

# Ejecutar
if __name__ == "__main__":
    run_etl()
