"""create roles model

Revision ID: 98d514c1dcb2
Revises: f8f3855f6900
Create Date: 2024-07-26 11:09:26.282290

"""
from alembic import op
import sqlalchemy as sa


revision = '98d514c1dcb2'
down_revision = 'f8f3855f6900'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('role',
    sa.Column('id', sa.Integer(), nullable=False),
            sa.Column('name', sa.String(), nullable=False),
            sa.PrimaryKeyConstraint('id', name=op.f('pk_role')),
            sa.UniqueConstraint('name', name=op.f('uq_role_name'))
    )
    op.add_column('user', sa.Column('role_id', sa.Integer(), nullable=False))
    op.create_foreign_key(op.f('fk_user_role_id_role'), 'user', 'role', ['role_id'], ['id'], ondelete='cascade')


def downgrade():
    op.drop_constraint(op.f('fk_user_role_id_role'), 'user', type_='foreignkey')
    op.drop_column('user', 'role_id')
    op.drop_table('role')
