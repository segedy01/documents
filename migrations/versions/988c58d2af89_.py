"""empty message

Revision ID: 988c58d2af89
Revises: 
Create Date: 2017-04-05 19:30:48.101998

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '988c58d2af89'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('document_meta_data',
    sa.Column('document_identifier', sa.String(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('Date', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('document_identifier')
    )
    op.create_index(op.f('ix_document_meta_data_name'), 'document_meta_data', ['name'], unique=False)
    op.create_table('users_document',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('document', sa.String(length=150), nullable=True),
    sa.Column('email', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['document'], ['document_meta_data.document_identifier'], ),
    sa.ForeignKeyConstraint(['email'], ['users.email'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('documents')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('documents',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.VARCHAR(length=150), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name=u'documents_pkey'),
    sa.UniqueConstraint('name', name=u'documents_name_key')
    )
    op.drop_table('users_document')
    op.drop_index(op.f('ix_document_meta_data_name'), table_name='document_meta_data')
    op.drop_table('document_meta_data')
    # ### end Alembic commands ###
