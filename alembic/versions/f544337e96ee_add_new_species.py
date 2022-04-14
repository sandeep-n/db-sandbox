"""add new species

Revision ID: f544337e96ee
Revises: 3226986bff25
Create Date: 2021-06-27 16:43:25.656629

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f544337e96ee'
down_revision = '3226986bff25'
branch_labels = None
depends_on = None


def upgrade():
    with op.get_context().autocommit_block():
        op.execute("ALTER TYPE species ADD VALUE 'Jaguar'")


def downgrade():
    pass
