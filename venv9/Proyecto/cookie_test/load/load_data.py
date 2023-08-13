import pandas as pd
import numpy as np
import re
import os

class DataRetriver:
    """
    A class for retrieving data from a given A file path and processing it for further analysis.

    Parameters:
        file_path (str): The file path from which the data will be loaded.

    Attributes:
        file_path (str): The file path from which the data will be loaded.
        """
    

    RETRIEVED_DATA = 'retrieved_data.csv' # File name for the retrieved data.

    def __init__(self, url, data_path):
        self.url = url
        self.DATASETS_DIR = data_path

    def retrieve_data(self):
        """
        Retrieves data from the specified path, processes it, and stores it in a CSV file.

        Returns:
            str: A message indicating the location of the stored data.
        """    
        # Loading data from specific URL
        data = pd.read_csv(self.url)




    def get_dataframe(self):
        df = pd.read_excel(self.file_path)
        return df

if __name__ == "__main__":
    dr = DataRetriver('/content/drive/MyDrive/VII/Acoustic_Extinguisher_Fire_Dataset.xlsx')
    df = dr.get_dataframe()
    print(df)




---
# Create a class called DataRetriver
class DataRetriver(object):

    # Initialize the class with the file path to the Excel spreadsheet
    def __init__(self, file_path):
        self.file_path = file_path

    # Get the DataFrame from the Excel spreadsheet
    def get_dataframe(self):
        df = pd.read_excel(self.file_path)
        return df

    # Save the DataFrame to a CSV file

    
    def save_dataframe_to_csv(self, df, filename):
        df.to_csv(filename, index=False)

# If this code is being run as the main program
if __name__ == "__main__":

    # Create a DataRetriver object
    dr = DataRetriver('/content/drive/MyDrive/VII/Acoustic_Extinguisher_Fire_Dataset.xlsx')

    # Get the DataFrame from the Excel spreadsheet
    df = dr.get_dataframe()

    # Save the DataFrame to a CSV file
    dr.save_dataframe_to_csv(df, 'dataretriver.csv')

---

    def retrieve_data(self):
            """
            Retrieves data from the specified URL, processes it, and stores it in a CSV file.

        Returns:
            str: A message indicating the location of the stored data.
        """
        # Loading data from specific URL
        data = pd.read_csv(self.url)






----

# Create a class called DataRetriver
class DataRetriver(object):

    # Initialize the class with the file path to the Excel spreadsheet
    def __init__(self, file_path):
        self.file_path = file_path

    # Get the DataFrame from the Excel spreadsheet
    def get_dataframe(self):
        df = pd.read_excel(self.file_path)
        return df

    # Save the DataFrame to a CSV file
    def save_dataframe_to_csv(self, df, filename):
        df.to_csv(filename, index=False)

# If this code is being run as the main program
if __name__ == "__main__":

    # Create a DataRetriver object
    dr = DataRetriver('/content/drive/MyDrive/VII/Acoustic_Extinguisher_Fire_Dataset.xlsx')

    # Get the DataFrame from the Excel spreadsheet
    df = dr.get_dataframe()

    # Save the DataFrame to a CSV file
    dr.save_dataframe_to_csv(df, 'dataretriver.csv')

class DataRetriever:
    """
    A class for retrieving data from a given URL and processing it for further analysis.

    Parameters:
        url (str): The URL from which the data will be loaded.

    Attributes:
        url (str): The URL from which the data will be loaded.

    Example usage:
    ```
    URL = 'https://www.openml.org/data/get_csv/16826755/phpMYEkMl'
    data_retriever = DataRetriever(URL, DATASETS_DIR)
    result = data_retriever.retrieve_data()
    print(result)
    ```
    """
    DROP_COLS = ['name', 'ticket', 'boat', 'body', 'home.dest']
    # DATASETS_DIR = './data/'  # Directory where data will be saved.
    RETRIEVED_DATA = 'retrieved_data.csv'  # File name for the retrieved data.

    def __init__(self, url, data_path):
        self.url = url
        self.DATASETS_DIR = data_path

    def retrieve_data(self):
        """
        Retrieves data from the specified URL, processes it, and stores it in a CSV file.

        Returns:
            str: A message indicating the location of the stored data.
        """
        # Loading data from specific URL
        data = pd.read_csv(self.url)

        # Create directory if it does not exist
        if not os.path.exists(self.DATASETS_DIR):
            os.makedirs(self.DATASETS_DIR)
            print(f"Directory '{self.DATASETS_DIR}' created successfully.")
        else:
            print(f"Directory '{self.DATASETS_DIR}' already exists.")

        # Save data to CSV file
        data.to_csv(self.DATASETS_DIR + self.RETRIEVED_DATA, index=False)

        return f'Data stored in {self.DATASETS_DIR + self.RETRIEVED_DATA}'

# Usage Example:
# URL = 'https://www.openml.org/data/get_csv/16826755/phpMYEkMl'
# data_retriever = DataRetriever(URL)
# result = data_retriever.retrieve_data()
# print(result)
