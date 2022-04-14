"""add TWO new species

Revision ID: 4301d9d29590
Revises: f544337e96ee
Create Date: 2021-06-28 09:17:01.244819

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4301d9d29590'
down_revision = 'f544337e96ee'
branch_labels = None
depends_on = None


def upgrade():
    with op.get_context().autocommit_block():
        op.execute("ALTER TYPE species ADD VALUE 'Lion'")
        op.execute("ALTER TYPE species ADD VALUE 'Cheetah'")


def downgrade():
    pass
