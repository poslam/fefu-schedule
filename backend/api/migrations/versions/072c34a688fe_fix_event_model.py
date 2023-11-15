"""fix event model

Revision ID: 072c34a688fe
Revises: c2d52f616946
Create Date: 2023-11-15 13:06:56.531521

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '072c34a688fe'
down_revision: Union[str, None] = 'c2d52f616946'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('event', sa.Column('spec', sa.Enum('lecture', 'lab_or_prac', 'unknown', name='facilityspec'), nullable=True))
    op.add_column('event', sa.Column('active', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('event', 'active')
    op.drop_column('event', 'spec')
    # ### end Alembic commands ###
