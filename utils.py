import pandas as pd

def read_stock(ticker: str, folder_path: str) -> pd.DataFrame:
    """
    Function that read the history of a stock from the stocks folder.

    @param ticker: ticker to read the data from.
    @folder_path: folder of the stocks.
    @return: df with the data.
    """
    try:
        df_stock = pd.read_csv(folder_path + ticker + '.csv', index_col=0)
        return df_stock

    except FileNotFoundError:
        print("File Doesn't Exist")