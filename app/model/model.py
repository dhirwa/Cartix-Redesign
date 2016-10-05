from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:password@localhost/cartixdb'
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
    cartix_financialInst=db.relationship('Cartix_financialInst',backref='cartix_province', lazy='dynamic')
    cartix_agent=db.relationship('Cartix_agent',backref='cartix_province',lazy='dynamic')


class Cartix_district(db.Model):
    ctxd_id = db.Column(db.Integer, primary_key = True)
    ctxd_name = db.Column(db.String(20))
    ctxd_province= db.Column(db.Integer, db.ForeignKey('cartix_province.ctxp_id'))
    cartix_sector=db.relationship('Cartix_sector',backref='cartix_district', lazy='dynamic')
    cartix_population = db.relationship('Cartix_population',backref='cartix_district',lazy='dynamic')
    cartix_savinggroup=db.relationship('Cartix_savinggroup',backref='cartix_district', lazy= 'dynamic')
    cartix_financialInst=db.relationship('Cartix_financialInst',backref='cartix_district', lazy='dynamic')
    cartix_agent=db.relationship('Cartix_agent',backref='cartix_district',lazy='dynamic')

class Cartix_sector(db.Model):
    ctxs_id = db.Column(db.Integer, primary_key = True)
    ctxs_name = db.Column(db.String(50))
    ctxs_district=db.Column(db.Integer, db.ForeignKey('cartix_district.ctxd_id'))
    cartix_population = db.relationship('Cartix_population',backref='cartix_sector',lazy='dynamic')
    cartix_savinggroup=db.relationship('Cartix_savinggroup',backref='cartix_sector', lazy= 'dynamic')
    cartix_financialInst=db.relationship('Cartix_financialInst',backref='cartix_sector', lazy='dynamic')
    cartix_agent=db.relationship('Cartix_agent',backref='cartix_sector',lazy='dynamic')


class Cartix_savinggroup(db.Model):
    ctxsg_id=db.Column(db.Integer, primary_key = True)
    ctxsg_name=db.Column(db.String(50))
    ctxsg_creationyear=db.Column(db.Integer)
    ctxsg_sector=db.Column(db.Integer, db.ForeignKey('cartix_sector.ctxs_id'))
    ctxsg_district=db.Column(db.Integer, db.ForeignKey('cartix_district.ctxd_id'))
    ctxsg_province=db.Column(db.Integer, db.ForeignKey('cartix_province.ctxp_id'))
    ctxsg_members=db.Column(db.Integer)
    ctxsg_female=db.Column(db.Integer)
    ctxsg_male=db.Column(db.Integer)
    ctxsg_fundingNgo = db.Column(db.String(50))
    ctxsg_partnerNgo = db.Column(db.String(50))
    ctxsg_amount=db.Column(db.Integer)
    ctxsg_outstLoan=db.Column(db.Integer)



class Cartix_financialInst(db.Model):
    ctxfn_id= db.Column(db.Integer, primary_key = True)
    ctxfn_name=db.Column(db.String(50))
    ctxfn_type=db.Column(db.String(50))
    ctxfn_sector=db.Column(db.Integer, db.ForeignKey('cartix_sector.ctxs_id'))
    ctxfn_district=db.Column(db.Integer, db.ForeignKey('cartix_district.ctxd_id'))
    ctxfn_province=db.Column(db.Integer, db.ForeignKey('cartix_province.ctxp_id'))



class Cartix_agent(db.Model):
    ctxa_id = db.Column(db.Integer, primary_key = True)
    ctxa_name = db.Column(db.String(50))
    ctxa_type = db.Column(db.String(50))
    ctxa_sector=db.Column(db.Integer, db.ForeignKey('cartix_sector.ctxs_id'))
    ctxa_district=db.Column(db.Integer, db.ForeignKey('cartix_district.ctxd_id'))
    ctxa_province=db.Column(db.Integer, db.ForeignKey('cartix_province.ctxp_id'))


class Cartix_population(db.Model):
    ctxpp_id=db.Column(db.Integer, primary_key = True)
    ctxpp_total=db.Column(db.Integer)
    ctxpp_male=db.Column(db.Integer)
    ctxpp_female=db.Column(db.Integer)
    ctxpp_province = db.Column(db.Integer, db.ForeignKey('cartix_province.ctxp_id'))
    ctxpp_district = db.Column(db.Integer, db.ForeignKey('cartix_district.ctxd_id'))
    ctxpp_sector = db.Column(db.Integer, db.ForeignKey('cartix_sector.ctxs_id'))


if __name__ == '__main__':
    manager.run()
