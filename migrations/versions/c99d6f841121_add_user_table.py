"""add_user_table

Revision ID: c99d6f841121
Revises: 09274024c7c9
Create Date: 2021-11-21 20:30:48.869938

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql.sqltypes import Enum

# revision identifiers, used by Alembic.
revision = 'c99d6f841121'
down_revision = '09274024c7c9'
branch_labels = None
depends_on = None



def upgrade():
    op.create_table('users',
    sa.Column('id',sa.String(length=120), nullable=False),
    sa.Column('kakao_id',sa.String(length=120), nullable=False),
    sa.Column('username',sa.String(length=120), nullable=False),
    sa.Column('email',sa.String(length=120), nullable=False),
    sa.Column('nickname',sa.String(length=120), nullable=False),
    sa.Column('dept_code',sa.String(length=120), nullable=False),
    sa.Column('student_year',sa.String(length=120), nullable=False),
    sa.Column('sex',sa.String(length=120), nullable=False),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('deleted_at', sa.DateTime(timezone=True), nullable=True),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_users'))
    
    )



def downgrade():
     op.drop_table('users')
