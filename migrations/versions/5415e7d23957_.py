"""empty message

Revision ID: 5415e7d23957
Revises: 
Create Date: 2018-10-04 16:40:44.828609

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5415e7d23957'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.Unicode(length=255), server_default='', nullable=False),
    sa.Column('first_name', sa.String(length=40), nullable=True),
    sa.Column('last_name', sa.Unicode(length=50), server_default='', nullable=False),
    sa.Column('is_active', sa.Boolean(), server_default='0', nullable=False),
    sa.Column('password_hash', sa.String(length=255), server_default='', nullable=False),
    sa.Column('last_login', sa.DateTime(), nullable=True),
    sa.Column('is_admin', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    # ### end Alembic commands ###