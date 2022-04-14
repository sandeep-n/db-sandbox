"""create kitty table

Revision ID: 848d098b5bff
Revises: 
Create Date: 2021-06-27 14:27:28.382395

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '848d098b5bff'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('kitties',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('species', sa.Enum('Puma', 'Tiger', 'Ocelot', name='species'), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    schema='playground'
                    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('kitties', schema='playground')
    # ### end Alembic commands ###