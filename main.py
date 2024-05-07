from pathlib import Path
from functions import process_data, read_extensions


def read_clean(file_path):
    # Identifica a extensão do arquivo usando pathlib
    file_extension = Path(file_path).suffix.lower()

    # Dicionário de funções de leitura para diferentes tipos de arquivo
    read_functions = {
        '.csv': read_extensions.read_csv,
        '.json': read_extensions.read_json,
        '.xlsx': read_extensions.read_excel,
        '.xls': read_extensions.read_excel,
        '.txt': read_extensions.read_txt
        # Adicione mais extensões e funções de leitura conforme necessário
    }

    # Verifica se a extensão está no dicionário
    if file_extension not in read_functions:
        raise ValueError("Extensão do arquivo não suportada.")

    # Lê o arquivo usando a função correspondente à sua extensão
    df = read_functions[file_extension](file_path)

    return df


def main():
    file_path = "H:\\TCD\\_PMF\\Módulo 2\\00\\PETR4.csv"
    df_cleaned = read_clean(file_path)

    # Exemplo de aplicação das funções de filtragem e deslocamento usando .loc()
    filtered_data_loc = process_data.filter_by_date(df_cleaned, start_date=None, end_date=None, columns=['Open', 'Close'])
    print("Exemplo de filtro por datas usando .loc():")
    print(filtered_data_loc.head())

    # Exemplo de aplicação das funções de filtragem e deslocamento usando .iloc()
    filtered_data_iloc = process_data.filter_by_index(df_cleaned, start_index=None, end_index=None, columns=None)
    print("\nExemplo de filtro por índices usando .iloc():")
    print(filtered_data_iloc.head())

    # Exemplo de aplicação da função de deslocamento usando .shift()
    shifted_data = process_data.shift_column(df_cleaned, 'Close', 1)
    print("\nExemplo de deslocamento de coluna usando .shift():")
    print(shifted_data.head())


if __name__ == "__main__":
    main()
