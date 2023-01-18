"""empty message

Revision ID: 1dce7d209326
Revises: d9d9a966f66d
Create Date: 2023-01-14 20:46:07.893290

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1dce7d209326'
down_revision = 'd9d9a966f66d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_index('ix_user_username')
        batch_op.create_index(batch_op.f('ix_user_username'), ['username'], unique=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_user_username'))
        batch_op.create_index('ix_user_username', ['username'], unique=False)

    # ### end Alembic commands ###
