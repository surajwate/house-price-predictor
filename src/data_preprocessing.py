import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
import seaborn as sns
import matplotlib.pyplot as plt


def load_data(file_path):
    """
    Load data from a file path and return a pandas dataframe.
    """
    return pd.read_csv(file_path)


def handle_missing_values(df):
    """
    Handle missing values in the dataframe.
    """
    numerical_cols = df.select_dtypes(include=['int64', 'float64']).columns
    categorical_cols = df.select_dtypes(include=['object']).columns

    numerical_imputer = SimpleImputer(strategy='mean')
    categorical_imputer = SimpleImputer(strategy='most_frequent')

    df[numerical_cols] = numerical_imputer.fit_transform(df[numerical_cols])
    df[categorical_cols] = categorical_imputer.fit_transform(df[categorical_cols])

    return df


def handle_outliers(df):
    """
    Detect and treat outliers in the dataframe.
    """
    for col in df.select_dtypes(include=['int64', 'float64']).columns:
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        df[col] = np.where(df[col] > upper_bound, upper_bound, np.where(df[col] < lower_bound, lower_bound, df[col]))

    return df


def encode_categorical_variables(df):
    """
    Encode categorical variables using one-hot encoding.
    """
    categorical_cols = df.select_dtypes(include=['object']).columns
    df = pd.get_dummies(df, columns=categorical_cols, drop_first=True)
    return df


def normalize_numerical_features(df):
    """
    Normalize numerical features using standard scaler.
    """
    numerical_cols = df.select_dtypes(include=['int64', 'float64']).columns
    scaler = StandardScaler()
    df[numerical_cols] = scaler.fit_transform(df[numerical_cols])
    return df

def preprocess_data(file_path, output_path):
    """
    Perform data preprocessing and save the preprocessed data to the output path.
    """
    # Load data
    df = load_data(file_path)

    # Handle missing values
    df = handle_missing_values(df)

    # Handle outliers
    df = handle_outliers(df)

    # Encode categorical variables
    df = encode_categorical_variables(df)

    # Normalize numerical features
    df = normalize_numerical_features(df)

    # Save the preprocessed data
    df.to_csv(output_path, index=False)

    print(f"Data preprocessing is completed. The preprocessed data is saved at {output_path}.")


if __name__ == "__main__":
    file_path = "data/raw/train.csv"
    output_path = "data/processed/house_prices_clean.csv"
    preprocess_data(file_path, output_path)
    