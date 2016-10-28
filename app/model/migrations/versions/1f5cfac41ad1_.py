"""empty message

Revision ID: 1f5cfac41ad1
Revises: 7dc87eef1652
Create Date: 2016-10-26 11:39:58.054667

"""

# revision identifiers, used by Alembic.
revision = '1f5cfac41ad1'
down_revision = '7dc87eef1652'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('cartix_telcoagent')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cartix_telcoagent',
    sa.Column('ctxa_id', sa.INTEGER(), nullable=False),
    sa.Column('ctxa_type', sa.VARCHAR(length=50), autoincrement=False, nullable=True),
    sa.Column('ctxa_count', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('ctxa_district', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('ctxa_province', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['ctxa_district'], [u'cartix_district.ctxd_id'], name=u'cartix_telcoagent_ctxa_district_fkey'),
    sa.ForeignKeyConstraint(['ctxa_province'], [u'cartix_province.ctxp_id'], name=u'cartix_telcoagent_ctxa_province_fkey'),
    sa.PrimaryKeyConstraint('ctxa_id', name=u'cartix_telcoagent_pkey')
    )
    ### end Alembic commands ###