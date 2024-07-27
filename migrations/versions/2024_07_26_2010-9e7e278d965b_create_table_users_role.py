"""create table users, role

Revision ID: 9e7e278d965b
Revises: 
Create Date: 2024-07-26 20:10:48.819806

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = '9e7e278d965b'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('role',
    sa.Column('id', sa.Integer(), nullable=False),
            sa.Column('name', sa.String(), nullable=False),
            sa.PrimaryKeyConstraint('id', name=op.f('pk_role')),
            sa.UniqueConstraint('name', name=op.f('uq_role_name'))
    )
    op.create_table('user',
    sa.Column('role_id', sa.Integer(), nullable=False),
            sa.Column('id', sa.Integer(), nullable=False),
            sa.Column('email', sa.String(length=320), nullable=False),
            sa.Column('hashed_password', sa.String(length=1024), nullable=False),
            sa.Column('is_active', sa.Boolean(), nullable=False),
            sa.Column('is_superuser', sa.Boolean(), nullable=False),
            sa.Column('is_verified', sa.Boolean(), nullable=False),

    sa.ForeignKeyConstraint(['role_id'], ['role.id'], name=op.f('fk_user_role_id_role'), ondelete='cascade'),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_user'))
    )
    op.create_index(op.f('ix_user_email'), 'user', ['email'], unique=True)


def downgrade() -> None:
    op.drop_index(op.f('ix_user_email'), table_name='user')
    op.drop_table('user')
    op.drop_table('role')
