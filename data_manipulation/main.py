"""Main functions"""

import argparse
import logging
import os

PGHOST = os.getenv('PGHOST')
PGPORT = os.getenv('PGPORT')
PGUSER = os.getenv('PGUSER')
PGPASSWORD = os.getenv('PGPASSWORD')
PGDATABASE = os.getenv('PGDATABASE')

CHHOST = os.getenv('CHHOST')
CHPORT = os.getenv('CHPORT')
CHUSER = os.getenv('CHUSER')
CHPASSWORD = os.getenv('CHPASSWORD')
CHDATABASE = os.getenv('CHDATABASE')

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

parser = argparse.ArgumentParser(
                    prog='ProgramName',
                    description='What the program does',
                    epilog='Text at the bottom of help')

parser.add_argument('--filename', help='data file name')


if __name__ == '__main__':

    args = parser.parse_args()

    data_path = os.path.join("./data", args.filename)
    logger.debug(data_path)

    connection_string = f'postgresql://{PGUSER}:{PGPASSWORD}@{PGHOST}/{PGDATABASE}'

    logger.debug('Connection to pg with connection string %s', connection_string)

    # with psycopg.connect(connection_string) as conn:
    #     with conn.cursor() as cur:
    #         cur.connection.execute(f"""
    #             COPY toto FROM '{data_path}' WITH (DELIMITER '\t')
    #         """)

    #         logger.info(cur.fetchall())

    # df = pd.read_csv(data_path, sep="\t")

    # print(df.head())

    # COPY table_name [ ( column_name [, ...] ) ]
    # FROM { 'filename' | PROGRAM 'command' | STDIN }
    # [ [ WITH ] ( option [, ...] ) ]
    # [ WHERE condition ]
