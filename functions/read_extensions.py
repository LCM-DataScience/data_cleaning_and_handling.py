import pandas as pd
from . import process_data


def read_json(file):
    # Lê o arquivo JSON
    df = pd.read_json(file)
    return df


def read_csv(file):
    # Lê o arquivo específico
    df = pd.read_csv(file)

    # Chama a função process_data do módulo process_data
    return process_data.process_data(df)


def read_excel(file):
    # Lê o arquivo Excel
    df = pd.read_excel(file)
    return process_data.process_data(df)


def read_txt(file):
    # Lê o arquivo de texto
    df = pd.read_csv(file, delimiter='\t')
    return process_data.process_data(df)
