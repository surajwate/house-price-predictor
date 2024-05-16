# Data Collection from Kaggle
# Note: Make sure you have the Kaggle API installed and configured (Details are in 1_data_collection.ipynb)

import os
import zipfile


def download_and_extract_data(competition, file_path):
    """
    Download and extract the data from Kaggle.

    Args:
        competition (str): The Kaggle competition identifier.
        file_path (str): The directory where the data will be downloaded and extracted.
    """
    # Download the dataset using Kaggle API
    # The command below will download the data to the specified file_path
    os.system(f'kaggle competitions download -c {competition} -p {file_path}')

    # Extract the downloaded zip file
    # Loop through the files in the file_path
    for file in os.listdir(file_path):
        if file.endswith('.zip'):
            with zipfile.ZipFile(os.path.join(file_path, file), 'r') as zip_ref:
                zip_ref.extractall(file_path)
            # Remove the zip file after extracting to save space
            os.remove(os.path.join(file_path, file))
            

if __name__ == '__main__':
    competition = "house-prices-advanced-regression-techniques"
    file_path = "data/raw/"

    # Create the directory if it does not exist
    if not os.path.exists(file_path):
        os.makedirs(file_path)

    # Download and extract the data
    download_and_extract_data(competition, file_path)
    print("Data downloaded and extracted successfully!")
