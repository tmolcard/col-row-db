"""Postgres tables sqlalchemy model"""
from sqlalchemy.orm import declarative_base


from alembic import context
from clickhouse_sqlalchemy.alembic.dialect import patch_alembic_version

# pylint: disable=too-few-public-methods

with patch_alembic_version(context=context):

    CHBase = declarative_base()
