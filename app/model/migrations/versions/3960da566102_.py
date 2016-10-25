"""empty message

Revision ID: 3960da566102
Revises: 748db30d9d69
Create Date: 2016-10-24 10:54:37.265892

"""

# revision identifiers, used by Alembic.
revision = '3960da566102'
down_revision = '748db30d9d69'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('cartix_savinggroup')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cartix_savinggroup',
    sa.Column('ctxsg_id', sa.INTEGER(), nullable=False),
    sa.Column('ctxsg_name', sa.VARCHAR(length=50), autoincrement=False, nullable=True),
    sa.Column('ctxsg_creationyear', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('ctxsg_sector', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('ctxsg_district', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('ctxsg_province', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('ctxsg_members', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('ctxsg_female', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('ctxsg_male', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('ctxsg_fundingngo', sa.VARCHAR(length=50), autoincrement=False, nullable=True),
    sa.Column('ctxsg_partnerngo', sa.VARCHAR(length=50), autoincrement=False, nullable=True),
    sa.Column('ctxsg_status', sa.VARCHAR(length=50), autoincrement=False, nullable=True),
    sa.Column('ctxsg_amount', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('ctxsg_outstloan', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['ctxsg_district'], [u'cartix_district.ctxd_id'], name=u'cartix_savinggroup_ctxsg_district_fkey'),
    sa.ForeignKeyConstraint(['ctxsg_province'], [u'cartix_province.ctxp_id'], name=u'cartix_savinggroup_ctxsg_province_fkey'),
    sa.ForeignKeyConstraint(['ctxsg_sector'], [u'cartix_sector.ctxs_id'], name=u'cartix_savinggroup_ctxsg_sector_fkey'),
    sa.PrimaryKeyConstraint('ctxsg_id', name=u'cartix_savinggroup_pkey')
    )
    ### end Alembic commands ###