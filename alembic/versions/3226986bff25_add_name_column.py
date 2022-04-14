"""add name column

Revision ID: 3226986bff25
Revises: 848d098b5bff
Create Date: 2021-06-27 16:34:20.499957

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3226986bff25'
down_revision = '848d098b5bff'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('kitties', sa.Column('name', sa.String), schema='playground')


def downgrade():
    op.drop_column('kitties', 'name', 'playground')
