"""book

Revision ID: 19e0e3fafae5
Revises: 542dffe013b2
Create Date: 2020-04-19 16:59:44.129317

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '19e0e3fafae5'
down_revision = '542dffe013b2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('book', sa.Column('author', sa.String(length=64), nullable=True))
    op.add_column('book', sa.Column('book_type', sa.String(length=128), nullable=True))
    op.add_column('book', sa.Column('date', sa.Date(), nullable=True))
    op.add_column('book', sa.Column('num_page', sa.Integer(), nullable=True))
    op.add_column('book', sa.Column('title', sa.String(length=128), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('book', 'title')
    op.drop_column('book', 'num_page')
    op.drop_column('book', 'date')
    op.drop_column('book', 'book_type')
    op.drop_column('book', 'author')
    # ### end Alembic commands ###
