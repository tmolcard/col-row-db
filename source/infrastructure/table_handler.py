"""Table handler"""

import abc
from typing import List

import pandas as pd
from sqlalchemy import create_engine, inspect
from clickhouse_driver import Client

from config.config_ch import CH_CONNECTION_STRING, CHDATABASE, CHHOST, CHPASSWORD, CHPORT, CHUSER
from config.config_pg import PG_CONNECTION_STRING


class TableHandler(abc.ABC):
    """Table handler"""
    def __init__(self, table_name: str, connection_string: str) -> None:
        self.table_name = table_name
        self.engine = create_engine(connection_string)

    def get_table_columns(self) -> List[dict]:
        """Return table columns as list of dictionary describing each columns"""
        inspector = inspect(self.engine)
        return inspector.get_columns(self.table_name)

    @abc.abstractmethod
    def upload_df_to_db(self, df: pd.DataFrame):
        """Upload pandas DataFrame into desired table."""


class PostgresTableHandler(TableHandler):
    """Postgres table handler"""
    def __init__(self, table_name) -> None:
        super().__init__(table_name, connection_string=PG_CONNECTION_STRING)

    def upload_df_to_db(self, df: pd.DataFrame):
        """Upload pandas DataFrame into desired table."""

        with self.engine.connect() as con:
            df.to_sql(name=self.table_name, con=con, index=False, if_exists="append")


class ClickhouseTableHandler(TableHandler):
    """Clickhouse table handler"""
    def __init__(self, table_name) -> None:
        super().__init__(table_name, connection_string=CH_CONNECTION_STRING)

    def upload_df_to_db(self, df: pd.DataFrame):
        """Upload pandas DataFrame into desired table."""

        chunk_size = int(131072/2)

        for i in range(0, df.shape[0], chunk_size):

            with Client(
                host=CHHOST,
                port=CHPORT,
                user=CHUSER,
                password=CHPASSWORD,
                database=CHDATABASE,
                # settings={"insert_block_size": 131072}
            ) as client:

                client.insert_dataframe(
                    f'INSERT INTO {self.table_name} VALUES',
                    df.loc[i:min(i+chunk_size, df.shape[0]), :],
                    # df,
                    settings={"use_numpy": True},
                )
