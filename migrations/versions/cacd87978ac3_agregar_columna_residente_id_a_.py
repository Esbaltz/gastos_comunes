"""Agregar columna residente_id a departamento

Revision ID: cacd87978ac3
Revises: 
Create Date: 2024-12-08 09:24:44.806970

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cacd87978ac3'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('pago')
    op.drop_table('solicitud')
    op.drop_table('personal')
    op.drop_table('edificio')
    op.drop_table('departamento')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('departamento',
    sa.Column('id_dep', sa.INTEGER(), nullable=False),
    sa.Column('numero', sa.INTEGER(), nullable=False),
    sa.Column('piso', sa.INTEGER(), nullable=False),
    sa.Column('tipo', sa.VARCHAR(length=35), nullable=False),
    sa.PrimaryKeyConstraint('id_dep')
    )
    op.create_table('edificio',
    sa.Column('id_e', sa.INTEGER(), nullable=False),
    sa.Column('nombre', sa.VARCHAR(length=35), nullable=False),
    sa.Column('ubicacion', sa.VARCHAR(length=80), nullable=False),
    sa.Column('cantPisos', sa.INTEGER(), nullable=False),
    sa.Column('cantDeptos', sa.INTEGER(), nullable=False),
    sa.PrimaryKeyConstraint('id_e')
    )
    op.create_table('personal',
    sa.Column('rut', sa.INTEGER(), nullable=False),
    sa.Column('nombre', sa.VARCHAR(length=35), nullable=False),
    sa.Column('cargo', sa.VARCHAR(length=50), nullable=False),
    sa.Column('horario', sa.DATETIME(), nullable=False),
    sa.PrimaryKeyConstraint('rut')
    )
    op.create_table('solicitud',
    sa.Column('id_s', sa.INTEGER(), nullable=False),
    sa.Column('tipo', sa.VARCHAR(length=20), nullable=False),
    sa.Column('fecha', sa.DATE(), nullable=False),
    sa.Column('estado', sa.VARCHAR(length=20), nullable=False),
    sa.Column('descripion', sa.VARCHAR(length=200), nullable=False),
    sa.PrimaryKeyConstraint('id_s')
    )
    op.create_table('pago',
    sa.Column('id_p', sa.INTEGER(), nullable=False),
    sa.Column('monto', sa.INTEGER(), nullable=False),
    sa.Column('fecha', sa.DATE(), nullable=False),
    sa.Column('estado', sa.VARCHAR(length=20), nullable=False),
    sa.PrimaryKeyConstraint('id_p')
    )
    # ### end Alembic commands ###
