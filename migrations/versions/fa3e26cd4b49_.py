"""empty message

Revision ID: fa3e26cd4b49
Revises: 0cb995f03f3b
Create Date: 2022-08-03 20:48:56.206594

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fa3e26cd4b49'
down_revision = '0cb995f03f3b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user_course', sa.Column('user_type', sa.String(length=128), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user_course', 'user_type')
    # ### end Alembic commands ###
