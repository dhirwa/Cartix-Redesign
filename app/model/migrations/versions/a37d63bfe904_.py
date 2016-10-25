"""empty message

Revision ID: a37d63bfe904
Revises: 078848f3b74d
Create Date: 2016-10-24 16:50:02.423586

"""

# revision identifiers, used by Alembic.
revision = 'a37d63bfe904'
down_revision = '078848f3b74d'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cartix_bank',
    sa.Column('ctxb_id', sa.Integer(), nullable=False),
    sa.Column('ctxb_province', sa.Integer(), nullable=True),
    sa.Column('ctxb_district', sa.Integer(), nullable=True),
    sa.Column('ctxb_sector', sa.Integer(), nullable=True),
    sa.Column('ctxb_name', sa.String(length=50), nullable=True),
    sa.Column('ctxb_branches', sa.String(length=50), nullable=True),
    sa.ForeignKeyConstraint(['ctxb_district'], ['cartix_district.ctxd_id'], ),
    sa.ForeignKeyConstraint(['ctxb_province'], ['cartix_province.ctxp_id'], ),
    sa.ForeignKeyConstraint(['ctxb_sector'], ['cartix_sector.ctxs_id'], ),
    sa.PrimaryKeyConstraint('ctxb_id')
    )
    op.drop_table('cartix_financial_inst')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cartix_financial_inst',
    sa.Column('ctxfn_id', sa.INTEGER(), nullable=False),
    sa.Column('ctxfn_name', sa.VARCHAR(length=50), autoincrement=False, nullable=True),
    sa.Column('ctxfn_type', sa.VARCHAR(length=50), autoincrement=False, nullable=True),
    sa.Column('ctxfn_sector', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('ctxfn_district', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('ctxfn_province', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['ctxfn_district'], [u'cartix_district.ctxd_id'], name=u'cartix_financial_inst_ctxfn_district_fkey'),
    sa.ForeignKeyConstraint(['ctxfn_province'], [u'cartix_province.ctxp_id'], name=u'cartix_financial_inst_ctxfn_province_fkey'),
    sa.ForeignKeyConstraint(['ctxfn_sector'], [u'cartix_sector.ctxs_id'], name=u'cartix_financial_inst_ctxfn_sector_fkey'),
    sa.PrimaryKeyConstraint('ctxfn_id', name=u'cartix_financial_inst_pkey')
    )
    op.drop_table('cartix_bank')
    ### end Alembic commands ###
