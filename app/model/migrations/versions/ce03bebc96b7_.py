"""empty message

Revision ID: ce03bebc96b7
Revises: 3a368c52f951
Create Date: 2016-10-25 11:01:51.075540

"""

# revision identifiers, used by Alembic.
revision = 'ce03bebc96b7'
down_revision = '3a368c52f951'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cartix_nonsacco',
    sa.Column('ctxnu_id', sa.Integer(), nullable=False),
    sa.Column('ctxnu_province', sa.Integer(), nullable=True),
    sa.Column('ctxnu_district', sa.Integer(), nullable=True),
    sa.Column('ctxnu_sector', sa.Integer(), nullable=True),
    sa.Column('ctxnu_name', sa.String(length=50), nullable=True),
    sa.ForeignKeyConstraint(['ctxnu_district'], ['cartix_district.ctxd_id'], ),
    sa.ForeignKeyConstraint(['ctxnu_province'], ['cartix_province.ctxp_id'], ),
    sa.ForeignKeyConstraint(['ctxnu_sector'], ['cartix_sector.ctxs_id'], ),
    sa.PrimaryKeyConstraint('ctxnu_id')
    )
    op.create_table('cartix_sacco',
    sa.Column('ctxsc_id', sa.Integer(), nullable=False),
    sa.Column('ctxsc_province', sa.Integer(), nullable=True),
    sa.Column('ctxsc_district', sa.Integer(), nullable=True),
    sa.Column('ctxsc_sector', sa.Integer(), nullable=True),
    sa.Column('ctxsc_name', sa.String(length=50), nullable=True),
    sa.ForeignKeyConstraint(['ctxsc_district'], ['cartix_district.ctxd_id'], ),
    sa.ForeignKeyConstraint(['ctxsc_province'], ['cartix_province.ctxp_id'], ),
    sa.ForeignKeyConstraint(['ctxsc_sector'], ['cartix_sector.ctxs_id'], ),
    sa.PrimaryKeyConstraint('ctxsc_id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('cartix_sacco')
    op.drop_table('cartix_nonsacco')
    ### end Alembic commands ###