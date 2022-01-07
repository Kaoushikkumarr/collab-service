"""empty message

Revision ID: 51657317f8f3
Revises: 493fbb916292
Create Date: 2020-12-07 16:14:53.623094

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '51657317f8f3'
down_revision = '493fbb916292'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('collaboration__model', sa.Column('add_members', sa.String(), nullable=True))
    op.add_column('collaboration__model', sa.Column('demand_id', sa.String(), nullable=True))
    op.add_column('collaboration__model', sa.Column('public_access', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('collaboration__model', 'public_access')
    op.drop_column('collaboration__model', 'demand_id')
    op.drop_column('collaboration__model', 'add_members')
    # ### end Alembic commands ###