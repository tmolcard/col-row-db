"""Data loader"""

import abc
import csv
import os
from typing import Dict

import pandas as pd
from config.config_ch import CH_DB_TYPES
from config.config_pg import PG_DB_TYPES

from data import DATA_PATH


class DataLoader(abc.ABC):
    """Data loader"""

    def __init__(self, table_name: str, db_types: Dict[str, type]) -> None:
        self.db_types = db_types
        self.table_name = table_name

    def _utf8_length(self, value: str) -> int:
        return len(value.encode('utf-8') if value else "")

    def _format_dataframe(self, table_columns, df: pd.DataFrame, inplace: bool = False) -> pd.DataFrame:
        """Format columns."""
        if not inplace:
            df = df.copy()

        array_cols = [col for col in table_columns if isinstance(col['type'], self.db_types['array'])]
        for col in array_cols:
            df.loc[:, col['name']] = df.loc[:, col['name']].fillna("").apply(lambda x: x.split(','))
            items_string_length = df[col['name']].apply(
                lambda x: max(self._utf8_length(name) for name in x) if x else 0
            )
            df = df.loc[items_string_length < col['type'].item_type.length, :]

        int_cols = [col for col in table_columns if isinstance(col['type'], self.db_types['integer'])]
        for col in int_cols:
            df.loc[~df[col['name']].isna(), col['name']] = df.loc[~df[col['name']].isna(), col['name']].astype(int)

        boolean_cols = [col for col in table_columns if isinstance(col['type'], self.db_types['boolean'])]
        for col in boolean_cols:
            df.loc[~df[col['name']].isna(), col['name']] = df.loc[~df[col['name']].isna(), col['name']].astype(bool)

        string_cols = [col for col in table_columns if isinstance(col['type'], self.db_types['string'])]
        for col in string_cols:
            string_length = df[col['name']].fillna("").apply(self._utf8_length)
            df = df.loc[string_length < col['type'].length, :]

        return df

    def get_formatted_df_from_csv(self, table_columns: list) -> pd.DataFrame:
        """Load data from csv file into a pandas DataFrame."""

        type_mapping = {
            self.db_types['array']: str,
            self.db_types['string']: str,
            self.db_types['integer']: float,
            self.db_types['float']: float,
            self.db_types['boolean']: float,
        }

        table_columns_pandas = {col['name']: type_mapping[type(col['type'])] for col in table_columns}

        data_path = os.path.join(DATA_PATH, f"{self.table_name}.tsv")

        df = pd.read_csv(
            data_path, header=0, sep='\t', na_values=r"\N", quoting=csv.QUOTE_NONE, dtype=table_columns_pandas,
            on_bad_lines='warn'
        )

        return self._format_dataframe(table_columns=table_columns, df=df, inplace=True)


class ClickhouseDataLoader(DataLoader):
    """Clickhouse data loader"""
    def __init__(self, table_name: str) -> None:
        super().__init__(table_name, CH_DB_TYPES)


class PostgresDataLoader(DataLoader):
    """Postgres data loader"""
    def __init__(self, table_name: str) -> None:
        super().__init__(table_name, PG_DB_TYPES)
