"""add post

Revision ID: 4b1b596db73b
Revises: cac8ffca5448
Create Date: 2016-05-05 22:24:05.324654

"""

# revision identifiers, used by Alembic.
revision = '4b1b596db73b'
down_revision = 'cac8ffca5448'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('posts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=100), nullable=False),
    sa.Column('content', sa.Text(), nullable=False),
    sa.Column('date', sa.Date(), nullable=False),
    sa.Column('date_created', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('posts')
    ### end Alembic commands ###
