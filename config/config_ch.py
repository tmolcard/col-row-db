"""Clickhouse database config"""

import os
from typing import Dict

from clickhouse_sqlalchemy.types import Boolean, Int32, Float32, String, Array


# Databases connection parameters
CHHOST = os.getenv('CHHOST')
CHPORT = os.getenv('CHPORT')
CHUSER = os.getenv('CHUSER')
CHPASSWORD = os.getenv('CHPASSWORD')
CHDATABASE = os.getenv('CHDATABASE')

CH_CONNECTION_STRING = f"clickhouse+native://{CHUSER}:{CHPASSWORD}@{CHHOST}:{CHPORT}/{CHDATABASE}"

# CH model types
CH_DB_TYPES: Dict[str, type] = {
    "array": Array,
    "string": String,
    "integer": Int32,
    "float": Float32,
    "boolean": Boolean,
}

# CH_TYPE_MAPPING: Dict[str, type] = {
#     Array: str,
#     String: str,
#     Int32: float,
#     Float: float,
#     Boolean: float,
# }
