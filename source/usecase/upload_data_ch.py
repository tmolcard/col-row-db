"""Upload data from csv to clickhouse databases"""

import argparse
import logging
from config.dataset import DATASET_NAME_SET

from source.infrastructure.data_loader import ClickhouseDataLoader
from source.infrastructure.table_handler import ClickhouseTableHandler


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


parser = argparse.ArgumentParser(prog='UploadData', description='Upload data to database')

parser.add_argument('--dataset', help='data file name')

if __name__ == '__main__':

    args = parser.parse_args()
    dataset: str = args.dataset

    if dataset not in DATASET_NAME_SET:
        raise ValueError(f"Dataset '{dataset}' does not exists.")

    ch_table_handler = ClickhouseTableHandler(table_name=dataset)
    ch_data_loader = ClickhouseDataLoader(table_name=dataset)

    table_columns = ch_table_handler.get_table_columns()
    df = ch_data_loader.get_formatted_df_from_csv(table_columns=table_columns)
    ch_table_handler.upload_df_to_db(df=df)
