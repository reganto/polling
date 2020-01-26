"""add a column to users table

Revision ID: 83171505938a
Revises: 
Create Date: 2020-01-25 19:27:02.251906

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '83171505938a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.add_column(
        'users',
        sa.Column('password', sa.String(200), nullable=False),
    )


def downgrade():
    op.drop_column('users', 'password')
