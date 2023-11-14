"""facility model

Revision ID: e251ae4cd51c
Revises: bf5e0e0946ff
Create Date: 2023-11-14 12:40:01.616276

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e251ae4cd51c'
down_revision: Union[str, None] = 'bf5e0e0946ff'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('facility', sa.Column('capacity', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('facility', 'capacity')
    # ### end Alembic commands ###
