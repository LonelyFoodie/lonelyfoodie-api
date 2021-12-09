"""Add restaurant

Revision ID: 3c5c279caa93
Revises: 1c4f52ee49bd
Create Date: 2021-11-13 02:21:29.140240

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3c5c279caa93'
down_revision = '1c4f52ee49bd'
branch_labels = None
depends_on = None



def upgrade():
    op.create_table('restaurants',
    sa.Column('id', sa.String(length=120), nullable=False),
    sa.Column('name', sa.String(length=120), nullable=False),
    sa.Column('kakaomap_id', sa.String(length=120), nullable=True),
    sa.Column('reviews', sa.String(length=120), nullable=True),
    sa.Column('rating_avg', sa.Float(), nullable=True),
    sa.Column('latitude', sa.Float(), nullable=True),
    sa.Column('longitude', sa.Float(), nullable=True),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('deleted_at', sa.DateTime(timezone=True), nullable=True),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_restaurants'))
    )



def downgrade():
    op.drop_table('restaurants')
