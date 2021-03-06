"""new feilds in user model

Revision ID: 9a77fc014707
Revises: e1d20cbe5a4e
Create Date: 2022-04-10 20:11:08.974961

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9a77fc014707'
down_revision = 'e1d20cbe5a4e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('last_seen', sa.DateTime(), nullable=True))
    op.add_column('user', sa.Column('about_me', sa.String(length=140), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'about_me')
    op.drop_column('user', 'last_seen')
    # ### end Alembic commands ###
