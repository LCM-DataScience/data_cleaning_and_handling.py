import pandas as pd


def process_data(df):
    # Verifica se as colunas estão separadas por ponto e vírgula
    if ';' in df.columns[0]:
        df[['Date', 'Adj Close']] = df.iloc[:, 0].str.split(';', expand=True)
        df.drop(columns=[df.columns[0]], inplace=True)

    # Verifica se a coluna "Date" está presente no DataFrame
    if 'Date' not in df.columns:
        raise ValueError("Nenhuma coluna 'Date' encontrada no arquivo.")

    # Converte a coluna "Date" para datetime e usa como índice
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce', format='%Y-%m-%d')
    df.set_index('Date', inplace=True)

    # Remove NAs e NaNs
    df.dropna(inplace=True)

    # Ordena o DataFrame pelo índice (Data)
    df.sort_index(inplace=True)

    return df


# Filtro .loc
def filter_by_date(df, start_date, end_date, columns=None):
    filtered_df = df.loc[start_date:end_date, columns] if columns else df.loc[start_date:end_date]
    return filtered_df


# Filtro .iloc
def filter_by_index(df, start_index, end_index, columns=None):
    filtered_df = df.iloc[start_index:end_index, columns] if columns else df.iloc[start_index:end_index]
    return filtered_df


# Método .shift
def shift_column(df, column, shift_periods):
    new_column_name = f"{column}_shifted_{shift_periods}"
    df[new_column_name] = df[column].shift(shift_periods)
    return df
