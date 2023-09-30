"""Postgres database config"""

import os
from typing import Dict

from sqlalchemy.dialects.postgresql import BOOLEAN, INTEGER, VARCHAR, ARRAY, DOUBLE_PRECISION


# Databases connection parameters
PGHOST = os.getenv('PGHOST')
PGPORT = os.getenv('PGPORT')
PGUSER = os.getenv('PGUSER')
PGPASSWORD = os.getenv('PGPASSWORD')
PGDATABASE = os.getenv('PGDATABASE')

PG_CONNECTION_STRING = f'postgresql://{PGUSER}:{PGPASSWORD}@{PGHOST}/{PGDATABASE}'

# PG model types
PG_DB_TYPES: Dict[str, type] = {
    "array": ARRAY,
    "string": VARCHAR,
    "integer": INTEGER,
    "float": DOUBLE_PRECISION,
    "boolean": BOOLEAN,
}


# # PG model type mapping
# PG_TYPE_MAPPING: Dict[type, type] = {
#     ARRAY: str,
#     VARCHAR: str,
#     INTEGER: float,
#     FLOAT: float,
#     DOUBLE_PRECISION: float,
#     BOOLEAN: float,
# }
