"""Upload data from csv to postgres databases"""

import argparse
import logging
from config.dataset import DATASET_NAME_SET

from source.infrastructure.data_loader import PostgresDataLoader
from source.infrastructure.table_handler import PostgresTableHandler


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


parser = argparse.ArgumentParser(prog='UploadData', description='Upload data to database')

parser.add_argument('--dataset', help='data file name')

if __name__ == '__main__':

    args = parser.parse_args()
    dataset: str = args.dataset

    if dataset not in DATASET_NAME_SET:
        raise ValueError(f"Dataset '{dataset}' does not exists.")

    pg_table_handler = PostgresTableHandler(table_name=dataset)
    pg_data_loader = PostgresDataLoader(table_name=dataset)

    table_columns = pg_table_handler.get_table_columns()
    df = pg_data_loader.get_formatted_df_from_csv(table_columns=table_columns)
    pg_table_handler.upload_df_to_db(df=df)
