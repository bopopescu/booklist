"""book

Revision ID: 542dffe013b2
Revises: 877deee6e287
Create Date: 2020-04-16 01:45:38.103826

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '542dffe013b2'
down_revision = '877deee6e287'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('book', sa.Column('author', sa.String(length=64), nullable=True))
    op.add_column('book', sa.Column('book_type', sa.String(length=128), nullable=True))
    op.add_column('book', sa.Column('date', sa.DateTime(), nullable=True))
    op.add_column('book', sa.Column('num_page', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('book', 'num_page')
    op.drop_column('book', 'date')
    op.drop_column('book', 'book_type')
    op.drop_column('book', 'author')
    # ### end Alembic commands ###
