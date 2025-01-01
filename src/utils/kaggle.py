import pandas as pd
import kagglehub
import shutil
import os
from src.utils.helpers import get_absolute_path
from sklearn.preprocessing import OneHotEncoder


def download_data_from_kaggle(url: str):
    try:
        source_dir = kagglehub.dataset_download(url)
        destination_dir = get_absolute_path("data/raw")
        print("✅ Download completed successfully")

        # ensure the destination directory exists
        os.makedirs(destination_dir, exist_ok=True)

        # list all files in the source directory
        files = os.listdir(source_dir)

        for file in files:
            source_file = os.path.join(source_dir, file)
            destination_file = os.path.join(destination_dir, file)

            if os.path.isfile(source_file):
                shutil.copy(source_file, destination_file)
                print(f"✅ '{file}' copied successfully")
    except Exception as e:
        print(f"❌ An error occurred:\n{e}")


def read_data_set(path: str) -> pd.DataFrame:
    data_path = get_absolute_path(path)

    if not os.path.exists(data_path):
        print(f"❌ File not found: {data_path}")
        return
    data = pd.read_csv(data_path)
    df = pd.DataFrame(data)
    return df


def one_hot_encode(df: pd.DataFrame):
    categorical_cols = df.select_dtypes(include=["object"]).columns.tolist()
    encoder = OneHotEncoder(sparse_output=False, handle_unknown="ignore")
    one_hot_encoded = encoder.fit_transform(df[categorical_cols])
    one_hot_encoded = pd.DataFrame(
        one_hot_encoded,
        columns=encoder.get_feature_names_out(categorical_cols),
        index=df.index,
    )

    # drop original columns and concatenate the encoded DataFrame
    df.drop(categorical_cols, axis=1, inplace=True)
    df = pd.concat([df, one_hot_encoded], axis=1)
    return df
