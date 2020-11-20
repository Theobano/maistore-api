"""empty message

Revision ID: ff4c3b09226e
Revises: 022d274ee1f6
Create Date: 2020-11-19 22:35:46.678405

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ff4c3b09226e'
down_revision = '022d274ee1f6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('product', 'is_available')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('product', sa.Column('is_available', sa.BOOLEAN(), autoincrement=False, nullable=False))
    # ### end Alembic commands ###
