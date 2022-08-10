"""empty message

Revision ID: d3be7cce4ee0
Revises: 6ad41db4c4c8
Create Date: 2022-08-09 18:20:35.742763

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd3be7cce4ee0'
down_revision = '6ad41db4c4c8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('app_user', 'about_me')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('app_user', sa.Column('about_me', sa.VARCHAR(length=1024), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
