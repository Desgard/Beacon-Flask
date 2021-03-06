"""empty message

Revision ID: 5f65fb22f45e
Revises: 
Create Date: 2017-05-25 11:08:49.720258

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5f65fb22f45e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Histories',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('video_id', sa.Integer(), nullable=True),
    sa.Column('watch_date', sa.DateTime(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_Histories_user_id'), 'Histories', ['user_id'], unique=False)
    op.create_table('Types',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('type_id', sa.Integer(), nullable=True),
    sa.Column('desc', sa.String(length=30), nullable=True),
    sa.Column('name', sa.String(length=30), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_Types_type_id'), 'Types', ['type_id'], unique=False)
    op.create_table('Users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('uuid', sa.String(length=20), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_Users_uuid'), 'Users', ['uuid'], unique=False)
    op.create_table('Videos',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('video_id', sa.String(length=20), nullable=True),
    sa.Column('title', sa.String(length=50), nullable=True),
    sa.Column('short_title', sa.String(length=50), nullable=True),
    sa.Column('img', sa.String(length=1000), nullable=True),
    sa.Column('sns_score', sa.String(length=100), nullable=True),
    sa.Column('play_count', sa.String(length=100), nullable=True),
    sa.Column('play_count_text', sa.String(length=20), nullable=True),
    sa.Column('a_id', sa.String(length=20), nullable=True),
    sa.Column('tv_id', sa.String(length=20), nullable=True),
    sa.Column('is_vip', sa.String(length=10), nullable=True),
    sa.Column('type', sa.String(length=20), nullable=True),
    sa.Column('p_type', sa.String(length=10), nullable=True),
    sa.Column('date_timestamp', sa.String(length=20), nullable=True),
    sa.Column('date_format', sa.String(length=20), nullable=True),
    sa.Column('total_num', sa.String(length=10), nullable=True),
    sa.Column('update_num', sa.String(length=10), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_Videos_video_id'), 'Videos', ['video_id'], unique=True)
    op.create_table('UserVideoRelation',
    sa.Column('videos_id', sa.Integer(), nullable=True),
    sa.Column('users_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['users_id'], ['Users.id'], ),
    sa.ForeignKeyConstraint(['videos_id'], ['Videos.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('UserVideoRelation')
    op.drop_index(op.f('ix_Videos_video_id'), table_name='Videos')
    op.drop_table('Videos')
    op.drop_index(op.f('ix_Users_uuid'), table_name='Users')
    op.drop_table('Users')
    op.drop_index(op.f('ix_Types_type_id'), table_name='Types')
    op.drop_table('Types')
    op.drop_index(op.f('ix_Histories_user_id'), table_name='Histories')
    op.drop_table('Histories')
    # ### end Alembic commands ###
