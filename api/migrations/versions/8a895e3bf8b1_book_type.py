"""book_type

Revision ID: 8a895e3bf8b1
Revises: 19e0e3fafae5
Create Date: 2020-04-20 10:51:38.291435

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8a895e3bf8b1'
down_revision = '19e0e3fafae5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('book_type', sa.Column('name', sa.String(length=64), nullable=True))
    op.add_column('book_type', sa.Column('status', sa.Boolean(), nullable=True))
    op.create_unique_constraint(None, 'book_type', ['name'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'book_type', type_='unique')
    op.drop_column('book_type', 'status')
    op.drop_column('book_type', 'name')
    op.drop_constraint(None, 'book', type_='foreignkey')
    # ### end Alembic commands ###