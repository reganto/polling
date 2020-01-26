"""add default value for password

Revision ID: 58a016cf87f2
Revises: 83171505938a
Create Date: 2020-01-25 19:39:57.241914

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '58a016cf87f2'
down_revision = '83171505938a'
branch_labels = None
depends_on = None


def upgrade():
    op.alter_column(
        'users',
        sa.column('password', sa.String(200), default=' ')
    )


def downgrade():
    pass
