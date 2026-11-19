import pytest
from src.datas_main import datas_load_csv
import pandas as pd

def test_datas_load_csv(tmp_path):
    # create a temporary CSV
    csv_path = tmp_path / "test.csv"
    csv_path.write_text("a,b\n1,2\n3,4\n")
    df = datas_load_csv(str(csv_path))
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (2, 2)
    assert list(df.columns) == ["a", "b"]
