"""empty message

Revision ID: 5ced25728524
Revises: 51657317f8f3
Create Date: 2020-12-09 17:19:43.214738

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '5ced25728524'
down_revision = '51657317f8f3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('collaboration__model', sa.Column('feedback', postgresql.JSONB(astext_type=sa.Text()), nullable=True))
    op.add_column('collaboration__model', sa.Column('is_hide', sa.Boolean(), nullable=True))
    op.drop_column('collaboration__model', 'public_access')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('collaboration__model', sa.Column('public_access', sa.BOOLEAN(), autoincrement=False, nullable=True))
    op.drop_column('collaboration__model', 'is_hide')
    op.drop_column('collaboration__model', 'feedback')
    # ### end Alembic commands ###
