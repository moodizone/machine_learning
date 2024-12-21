import pandas as pd
import kagglehub
import shutil
import os
from src.utils.helpers import get_absolute_path


def store_data_set():
    """
    Dataset characteristics:
    https://www.kaggle.com/datasets/kumarajarshi/life-expectancy-who
    """
    try:
        source_dir = kagglehub.dataset_download("kumarajarshi/life-expectancy-who")
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


def read_data_set() -> pd.DataFrame:
    data_path = get_absolute_path("data/raw/Life Expectancy Data.csv")

    if not os.path.exists(data_path):
        print(f"❌ File not found: {data_path}")
        return
    data = pd.read_csv(data_path)
    df = pd.DataFrame(data)
    return df
