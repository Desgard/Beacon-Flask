"""inital migration

Revision ID: 6420a9090c9c
Revises: 
Create Date: 2017-05-22 00:06:16.522831

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6420a9090c9c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('sqlite_stat1')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('sqlite_stat1',
    sa.Column('tbl', sa.NullType(), nullable=True),
    sa.Column('idx', sa.NullType(), nullable=True),
    sa.Column('stat', sa.NullType(), nullable=True)
    )
    # ### end Alembic commands ###