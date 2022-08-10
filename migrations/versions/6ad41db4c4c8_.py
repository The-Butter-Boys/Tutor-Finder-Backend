"""empty message

Revision ID: 6ad41db4c4c8
Revises: fa3e26cd4b49
Create Date: 2022-08-09 17:23:42.272270

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6ad41db4c4c8'
down_revision = 'fa3e26cd4b49'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('app_user', sa.Column('about_me', sa.String(length=1024), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('app_user', 'about_me')
    # ### end Alembic commands ###
