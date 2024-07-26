"""create users model

Revision ID: f8f3855f6900
Revises: 
Create Date: 2024-07-26 10:00:15.814511

"""
from alembic import op
import sqlalchemy as sa


revision = 'f8f3855f6900'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
            sa.Column('email', sa.String(length=320), nullable=False),
            sa.Column('hashed_password', sa.String(length=1024), nullable=False),
            sa.Column('is_active', sa.Boolean(), nullable=False),
            sa.Column('is_superuser', sa.Boolean(), nullable=False),
            sa.Column('is_verified', sa.Boolean(), nullable=False),
            sa.PrimaryKeyConstraint('id', name=op.f('pk_user'))
    )
    op.create_index(op.f('ix_user_email'), 'user', ['email'], unique=True)


def downgrade():
    op.drop_index(op.f('ix_user_email'), table_name='user')
    op.drop_table('user')
