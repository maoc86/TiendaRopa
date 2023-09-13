"""empty message

Revision ID: 8ab06a9e46eb
Revises: d64efafdad81
Create Date: 2023-09-12 17:36:15.228409

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8ab06a9e46eb'
down_revision = 'd64efafdad81'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cliente',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=120), nullable=False),
    sa.Column('apellido', sa.String(length=120), nullable=False),
    sa.Column('documento', sa.Integer(), nullable=False),
    sa.Column('direccion', sa.String(length=120), nullable=False),
    sa.Column('email', sa.String(length=80), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('apellido'),
    sa.UniqueConstraint('direccion'),
    sa.UniqueConstraint('documento'),
    sa.UniqueConstraint('nombre')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('cliente')
    # ### end Alembic commands ###