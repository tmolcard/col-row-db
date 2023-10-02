"""Postgre: Add index on title

Revision ID: ba3f0e134532
Revises: b1fe2784ca6f
Create Date: 2023-10-02 11:15:48.665007

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'ba3f0e134532'
down_revision = 'b1fe2784ca6f'
branch_labels = None
depends_on = None


def upgrade(engine_name: str) -> None:
    globals()["upgrade_%s" % engine_name]()


def downgrade(engine_name: str) -> None:
    globals()["downgrade_%s" % engine_name]()


def upgrade_postgresql() -> None:
    op.create_index('title_akas_title_index', 'title_akas', ['title'])
    op.create_index('title_basics_primary_title_index', 'title_basics', ['primary_title'])


def downgrade_postgresql() -> None:
    op.drop_index('title_akas_title_index', table_name='title_akas')
    op.drop_index('title_basics_primary_title_index', table_name='title_basics')


def upgrade_clickhouse() -> None:
    pass


def downgrade_clickhouse() -> None:
    pass