"""Create tables

Revision ID: 1905862cd882
Revises:
Create Date: 2024-11-16 22:24:12.763564

"""

from datetime import datetime
from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = '1905862cd882'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'users',
        sa.Column(
            'id', sa.Integer(), nullable=False, primary_key=True, index=True
        ),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column(
            'email', sa.String(), nullable=False, unique=True, index=True
        ),
        sa.Column('hashed_password', sa.String(), nullable=False),
        sa.Column('is_active', sa.Boolean(), nullable=False, default=True),
        sa.Column(
            'created_at', sa.DateTime(), nullable=False, default=datetime.utcnow
        ),
        sa.Column(
            'updated_at',
            sa.DateTime(),
            nullable=False,
            default=datetime.utcnow,
            onupdate=datetime.utcnow,
        ),
    )

    op.create_table(
        'summaries',
        sa.Column(
            'id', sa.Integer(), nullable=False, primary_key=True, index=True
        ),
        sa.Column('original_text', sa.Text(), nullable=False),
        sa.Column('summarized_text', sa.Text(), nullable=False),
        sa.Column('summary_length', sa.Integer(), nullable=True),
        sa.Column(
            'created_at', sa.DateTime(), nullable=False, default=datetime.utcnow
        ),
        sa.Column(
            'user_id',
            sa.Integer(),
            sa.ForeignKey('users.id', ondelete="CASCADE"),
            nullable=False,
        ),
    )


def downgrade() -> None:
    op.drop_table('summaries')
    op.drop_table('users')
