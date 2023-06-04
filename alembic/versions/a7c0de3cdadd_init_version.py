"""init version

Revision ID: a7c0de3cdadd
Revises: 
Create Date: 2023-04-25 13:40:17.435980

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a7c0de3cdadd'
down_revision = None
branch_labels = None
depends_on = None


def upgrade(engine_name: str) -> None:
    globals()["upgrade_%s" % engine_name]()


def downgrade(engine_name: str) -> None:
    globals()["downgrade_%s" % engine_name]()





def upgrade_postgresql() -> None:
    pass


def downgrade_postgresql() -> None:
    pass


def upgrade_clickhouse() -> None:
    pass


def downgrade_clickhouse() -> None:
    pass

