"""empty message

Revision ID: c6b3a386f119
Revises: 0a73da054ce3
Create Date: 2023-03-12 14:49:26.868665

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c6b3a386f119'
down_revision = '0a73da054ce3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('students_records', schema=None) as batch_op:
        batch_op.add_column(sa.Column('honours', sa.String(), nullable=True))
        batch_op.drop_column('honurs')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('students_records', schema=None) as batch_op:
        batch_op.add_column(sa.Column('honurs', sa.VARCHAR(), nullable=True))
        batch_op.drop_column('honours')

    # ### end Alembic commands ###
