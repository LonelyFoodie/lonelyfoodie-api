"""Delete demo tables

Revision ID: 09274024c7c9
Revises: 3c5c279caa93
Create Date: 2021-11-13 03:24:34.668428

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '09274024c7c9'
down_revision = '3c5c279caa93'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('posts')
    op.drop_table('categories')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('categories',
    sa.Column('id', sa.VARCHAR(length=120), autoincrement=False, nullable=False),
    sa.Column('name', sa.VARCHAR(length=50), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='pk_categories'),
    postgresql_ignore_search_path=False
    )
    op.create_table('posts',
    sa.Column('id', sa.VARCHAR(length=120), autoincrement=False, nullable=False),
    sa.Column('title', sa.VARCHAR(length=80), autoincrement=False, nullable=True),
    sa.Column('body', sa.VARCHAR(length=2000), autoincrement=False, nullable=True),
    sa.Column('pub_date', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('category_id', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['category_id'], ['categories.id'], name='fk_posts_category_id_categories'),
    sa.PrimaryKeyConstraint('id', name='pk_posts')
    )
    # ### end Alembic commands ###
