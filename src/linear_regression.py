import pandas as pd
from sklearn.datasets import load_diabetes

from src.utils.helpers import get_absolute_path


def store_raw_diabetes():
    """
    Dataset characteristics:
    https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_diabetes.html#sklearn.datasets.load_diabetes
    https://scikit-learn.org/stable/datasets/toy_dataset.html#diabetes-dataset
    """
    diabetes = load_diabetes(as_frame=False, return_X_y=False, scaled=False)
    df = pd.DataFrame(diabetes.data, columns=diabetes.feature_names)
    df["Target"] = diabetes.target
    df.to_csv("./data/raw/diabetes.csv", index=False)


def read_raw_diabetes() -> pd.DataFrame:
    data_path = get_absolute_path("data/raw/diabetes.csv")
    data = pd.read_csv(data_path)
    df = pd.DataFrame(data)
    return df
