"""event model fix

Revision ID: fbf109745469
Revises: 81d9e8c4cfb5
Create Date: 2023-10-28 20:35:42.548450

"""
from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = 'fbf109745469'
down_revision: Union[str, None] = '81d9e8c4cfb5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('event_facility_fkey', 'event', type_='foreignkey')
    op.drop_constraint('event_teacher_fkey', 'event', type_='foreignkey')
    op.drop_constraint('event_group_fkey', 'event', type_='foreignkey')
    op.alter_column('event', 'facility',
                    existing_type=sa.INTEGER(),
                    type_=sa.TEXT(),
                    existing_nullable=True)
    op.alter_column('event', 'group',
                    existing_type=sa.INTEGER(),
                    type_=sa.TEXT(),
                    existing_nullable=True)
    op.create_unique_constraint(None, 'facility', ['name'])
    op.create_unique_constraint(None, 'group', ['name'])
    op.create_unique_constraint(None, 'teacher', ['name'])
    op.create_foreign_key(None, 'event', 'facility', ['facility'], ['name'])
    op.create_foreign_key(None, 'event', 'teacher', ['teacher'], ['name'])
    op.create_foreign_key(None, 'event', 'group', ['group'], ['name'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'teacher', type_='unique')
    op.drop_constraint(None, 'group', type_='unique')
    op.drop_constraint(None, 'facility', type_='unique')
    op.drop_constraint(None, 'event', type_='foreignkey')
    op.drop_constraint(None, 'event', type_='foreignkey')
    op.drop_constraint(None, 'event', type_='foreignkey')
    op.create_foreign_key('event_group_fkey', 'event',
                          'group', ['group'], ['id'])
    op.create_foreign_key('event_teacher_fkey', 'event',
                          'teacher', ['teacher'], ['id'])
    op.create_foreign_key('event_facility_fkey', 'event',
                          'facility', ['facility'], ['id'])
    op.alter_column('event', 'group',
                    existing_type=sa.TEXT(),
                    type_=sa.INTEGER(),
                    existing_nullable=True)
    op.alter_column('event', 'facility',
                    existing_type=sa.TEXT(),
                    type_=sa.INTEGER(),
                    existing_nullable=True)
    # ### end Alembic commands ###
