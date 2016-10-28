from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:password@localhost/cartix'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cartix.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True


#$lldkld
db=SQLAlchemy(app)
migrate= Migrate(app, db)


manager=Manager(app)
manager.add_command('db', MigrateCommand)

class Cartix_province(db.Model):
    ctxp_id = db.Column(db.Integer, primary_key = True)
    ctxp_name = db.Column(db.String(20))
    cartix_district=db.relationship('Cartix_district',backref='cartix_province', lazy='dynamic')
    cartix_population = db.relationship('Cartix_population',backref='cartix_province',lazy='dynamic')
    cartix_savinggroup=db.relationship('Cartix_savinggroup',backref='cartix_province', lazy= 'dynamic')
    cartix_telcoagent=db.relationship('Cartix_telcoagent',backref='cartix_province',lazy='dynamic')
    cartix_bankagent = db.relationship('Cartix_bankagent',backref='cartix_province',lazy='dynamic')
    cartix_bank=db.relationship('Cartix_bank',backref='cartix_province',lazy='dynamic')
    cartix_mfi=db.relationship('Cartix_mfi',backref='cartix_province',lazy='dynamic')
    cartix_nonsacco=db.relationship('Cartix_nonsacco',backref='cartix_province',lazy='dynamic')
    cartix_sacco=db.relationship('Cartix_sacco',backref='cartix_province',lazy='dynamic')


class Cartix_district(db.Model):
    ctxd_id = db.Column(db.Integer, primary_key = True)
    ctxd_name = db.Column(db.String(20))
    ctxd_province= db.Column(db.Integer, db.ForeignKey('cartix_province.ctxp_id'))
    cartix_sector=db.relationship('Cartix_sector',backref='cartix_district', lazy='dynamic')
    cartix_population = db.relationship('Cartix_population',backref='cartix_district',lazy='dynamic')
    cartix_savinggroup=db.relationship('Cartix_savinggroup',backref='cartix_district', lazy= 'dynamic')
    cartix_telcoagent=db.relationship('Cartix_telcoagent',backref='cartix_district',lazy='dynamic')
    cartix_bankagent = db.relationship('Cartix_bankagent',backref='cartix_district',lazy='dynamic')
    cartix_bank=db.relationship('Cartix_bank',backref='cartix_district',lazy='dynamic')
    cartix_mfi=db.relationship('Cartix_mfi',backref='cartix_district',lazy='dynamic')
    cartix_nonsacco=db.relationship('Cartix_nonsacco',backref='cartix_district',lazy='dynamic')
    cartix_sacco=db.relationship('Cartix_sacco',backref='cartix_district',lazy='dynamic')

class Cartix_sector(db.Model):
    ctxs_id = db.Column(db.Integer, primary_key = True)
    ctxs_name = db.Column(db.String(50))
    ctxs_district=db.Column(db.Integer, db.ForeignKey('cartix_district.ctxd_id'))
    cartix_population = db.relationship('Cartix_population',backref='cartix_sector',lazy='dynamic')
    cartix_savinggroup=db.relationship('Cartix_savinggroup',backref='cartix_sector', lazy= 'dynamic')
    #cartix_telcoagent=db.relationship('Cartix_telcoagent',backref='cartix_sector',lazy='dynamic')
    #cartix_bankagent = db.relationship('Cartix_bankagent',backref='cartix_sector',lazy='dynamic')
    cartix_bank=db.relationship('Cartix_bank',backref='cartix_sector',lazy='dynamic')
    cartix_mfi=db.relationship('Cartix_mfi',backref='cartix_sector',lazy='dynamic')
    cartix_nonsacco=db.relationship('Cartix_nonsacco',backref='cartix_sector',lazy='dynamic')
    cartix_sacco=db.relationship('Cartix_sacco',backref='cartix_sector',lazy='dynamic')


class Cartix_savinggroup(db.Model):
    ctxsg_id=db.Column(db.Integer, primary_key = True)
    ctxsg_name=db.Column(db.String(50))
    ctxsg_creationyear=db.Column(db.Integer)
    ctxsg_sector=db.Column(db.Integer, db.ForeignKey('cartix_sector.ctxs_id'))
    ctxsg_district=db.Column(db.Integer, db.ForeignKey('cartix_district.ctxd_id'))
    ctxsg_province=db.Column(db.Integer, db.ForeignKey('cartix_province.ctxp_id'))
    ctxsg_members=db.Column(db.Integer)
    ctxsg_female=db.Column(db.Integer)
    ctxsg_male = db.Column(db.Integer)
    ctxsg_fundingngo = db.Column(db.String(50))
    ctxsg_partnerngo = db.Column(db.String(50))
    ctxsg_status  = db.Column(db.String(50))
    ctxsg_amount=db.Column(db.Float)
    ctxsg_outstloan=db.Column(db.Float)



class Cartix_bank(db.Model):
    ctxb_id = db.Column(db.Integer, primary_key = True)
    ctxb_province=db.Column(db.Integer, db.ForeignKey('cartix_province.ctxp_id'))
    ctxb_district=db.Column(db.Integer, db.ForeignKey('cartix_district.ctxd_id'))
    ctxb_sector=db.Column(db.Integer, db.ForeignKey('cartix_sector.ctxs_id'))
    ctxb_name=db.Column(db.String(100))
    ctxb_branches=db.Column(db.String(100))

class Cartix_nonsacco(db.Model):
    ctxnu_id = db.Column(db.Integer, primary_key=True)
    ctxnu_province=db.Column(db.Integer, db.ForeignKey('cartix_province.ctxp_id'))
    ctxnu_district=db.Column(db.Integer, db.ForeignKey('cartix_district.ctxd_id'))
    ctxnu_sector=db.Column(db.Integer, db.ForeignKey('cartix_sector.ctxs_id'))
    ctxnu_name=db.Column(db.String(50))


class Cartix_sacco(db.Model):
    ctxsc_id = db.Column(db.Integer, primary_key=True)
    ctxsc_province=db.Column(db.Integer, db.ForeignKey('cartix_province.ctxp_id'))
    ctxsc_district=db.Column(db.Integer, db.ForeignKey('cartix_district.ctxd_id'))
    ctxsc_sector=db.Column(db.Integer, db.ForeignKey('cartix_sector.ctxs_id'))
    ctxsc_name=db.Column(db.String(50))

class Cartix_mfi(db.Model):
        ctxm_id = db.Column(db.Integer, primary_key = True)
        ctxm_province=db.Column(db.Integer, db.ForeignKey('cartix_province.ctxp_id'))
        ctxm_district=db.Column(db.Integer, db.ForeignKey('cartix_district.ctxd_id'))
        ctxm_sector=db.Column(db.Integer, db.ForeignKey('cartix_sector.ctxs_id'))
        ctxm_name=db.Column(db.String(250))
        ctxm_count=db.Column(db.Integer)


class Cartix_telcoagent(db.Model):
    ctxa_id = db.Column(db.Integer, primary_key = True)
    ctxa_count = db.Column(db.Integer)
    ctxa_district=db.Column(db.Integer, db.ForeignKey('cartix_district.ctxd_id'))
    ctxa_province=db.Column(db.Integer, db.ForeignKey('cartix_province.ctxp_id'))


class Cartix_bankagent(db.Model):
    ctxba_id = db.Column(db.Integer, primary_key = True)
    ctxba_count = db.Column(db.Integer)
    ctxba_district=db.Column(db.Integer, db.ForeignKey('cartix_district.ctxd_id'))
    ctxba_province=db.Column(db.Integer, db.ForeignKey('cartix_province.ctxp_id'))

class Cartix_population(db.Model):
    ctxpp_id=db.Column(db.Integer, primary_key = True)
    ctxpp_total=db.Column(db.Integer)
    ctxpp_male=db.Column(db.Integer)
    ctxpp_female = db.Column(db.Integer)
    ctxpp_province = db.Column(db.Integer, db.ForeignKey('cartix_province.ctxp_id'))
    ctxpp_district = db.Column(db.Integer, db.ForeignKey('cartix_district.ctxd_id'))
    ctxpp_sector = db.Column(db.Integer, db.ForeignKey('cartix_sector.ctxs_id'))



if __name__ == '__main__':
    manager.run()
