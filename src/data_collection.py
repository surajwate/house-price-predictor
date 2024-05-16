# Data Collection from Kaggle

import os
import zipfile


def download_and_extract_data(competition, file_path):
    # Download the dataset using Kaggle API
    os.system(f'kaggle competitions download -c {competition} -p {file_path}')

    # Extract the downloaded zip file
    for file in os.listdir(file_path):
        if file.endswith('.zip'):
            with zipfile.ZipFile(os.path.join(file_path, file), 'r') as zip_ref:
                zip_ref.extractall(file_path)
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
