"""Initial Migration

Revision ID: e91b61c6c62b
Revises: 5bd202370d85
Create Date: 2020-10-26 17:07:40.759641

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e91b61c6c62b'
down_revision = '5bd202370d85'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('comments', sa.Column('comment', sa.String(length=255), nullable=True))
    op.drop_column('comments', 'commment')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('comments', sa.Column('commment', sa.VARCHAR(length=255), autoincrement=False, nullable=True))
    op.drop_column('comments', 'comment')
    # ### end Alembic commands ###
