"""book

Revision ID: c55ef8bf0f76
Revises: 8a895e3bf8b1
Create Date: 2020-04-20 11:14:08.172405

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'c55ef8bf0f76'
down_revision = '8a895e3bf8b1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('book', sa.Column('author', sa.String(length=64), nullable=True))
    op.add_column('book', sa.Column('book_type', sa.String(length=128), nullable=True))
    op.add_column('book', sa.Column('date', sa.Date(), nullable=True))
    op.add_column('book', sa.Column('num_page', sa.Integer(), nullable=True))
    op.add_column('book', sa.Column('title', sa.String(length=128), nullable=True))
    op.drop_column('book_type', 'status')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('book_type', sa.Column('status', mysql.TINYINT(display_width=1), autoincrement=False, nullable=True))
    op.drop_column('book', 'title')
    op.drop_column('book', 'num_page')
    op.drop_column('book', 'date')
    op.drop_column('book', 'book_type')
    op.drop_column('book', 'author')
    # ### end Alembic commands ###