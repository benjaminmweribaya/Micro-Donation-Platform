"""Updated models

Revision ID: 30f8cf09052b
Revises: 96a6e30087ff
Create Date: 2025-02-03 17:21:16.342558

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '30f8cf09052b'
down_revision = '96a6e30087ff'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('causes', schema=None) as batch_op:
        batch_op.add_column(sa.Column('category', sa.String(length=50), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('causes', schema=None) as batch_op:
        batch_op.drop_column('category')

    # ### end Alembic commands ###
