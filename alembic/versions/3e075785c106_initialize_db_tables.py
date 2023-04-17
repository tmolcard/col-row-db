"""initialize db tables

Revision ID: 3e075785c106
Revises:
Create Date: 2023-04-17 15:19:34.080260

"""
from alembic import op
import sqlalchemy as sa
import clickhouse_sqlalchemy as ch_sa
from clickhouse_sqlalchemy import engines


# revision identifiers, used by Alembic.
revision = '3e075785c106'
down_revision = None
branch_labels = None
depends_on = None


def upgrade(engine_name: str) -> None:
    globals()["upgrade_%s" % engine_name]()


def downgrade(engine_name: str) -> None:
    globals()["downgrade_%s" % engine_name]()


def upgrade_postgresql() -> None:
    op.create_table(
        'account',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(50), nullable=False),
        sa.Column('description', sa.Unicode(200)),
    )


def downgrade_postgresql() -> None:
    op.drop_table('account')


def upgrade_clickhouse() -> None:
    op.create_table(
        'account',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(50), nullable=False),
        sa.Column('description', sa.Unicode(200)),
        engines.MergeTree('id', order_by="id")
    )


def downgrade_clickhouse() -> None:
    op.drop_table('account')