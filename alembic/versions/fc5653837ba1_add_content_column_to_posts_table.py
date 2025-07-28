"""add content column to posts table

Revision ID: fc5653837ba1
Revises: 2a60ff77068f
Create Date: 2025-07-28 13:57:59.611004

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'fc5653837ba1'
down_revision: Union[str, Sequence[str], None] = '2a60ff77068f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column('posts', 'content')
    pass
