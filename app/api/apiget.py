from app import *
from app.model.model import *
from app.model.schema import *
import datetime
from sqlalchemy import func
from app.controllers.controller import *


@app.errorhandler(404)
def page_not_found(e):
    return 'Error 404: Page not found, Please check ur route well.'

@app.route('/getprovinces')
def get_prov():
    provs=Cartix_province.query.all()
    result=ctxps_schema.dump(provs)
    return jsonify({'Provinces':result.data})

@app.route('/getdistricts')
def get_dist():
    provs=Cartix_district.query.all()
    result=ctxds_schema.dump(provs)
    return jsonify({'Districts':result.data})

@app.route('/getsectors')
def get_sect():
    provs=Cartix_sector.query.all()
    result=ctxss_schema.dump(provs)
    return jsonify({'Sectors':result.data})

@app.route('/getpopulation')
def get_pop():
    provs=Cartix_population.query.all()
    result=ctxpps_schema.dump(provs)
    return jsonify({'Population':result.data})


@app.route('/getpopulation/sector/<int:sec>')
def get_pops(sec):
    provs=Cartix_population.query.filter_by(ctxpp_sector=sec).first()
    if provs :
        result=ctxpp_schema.dump(provs)
        return jsonify({'Message':'1','Sector population':result.data})
    else:
        return jsonify({'Message':'0'})


@app.route('/getpopulation/district/<int:dis>')
def get_popd(dis):
    provs=Cartix_population.query.filter_by(ctxpp_district=dis).all()
    if provs:
        json_data = ctxpps_schema.dump(provs).data
        pr,dis = get_sum(json_data, dis)
        return jsonify(pr)
    else:
        return jsonify({'Message':'0'})

@app.route('/getpopulation/province/<int:prov>')
def get_popp(prov):
    provs=Cartix_population.query.filter_by(ctxpp_province=prov).all()
    if provs :
        json_data = ctxpps_schema.dump(provs).data
        pr,prov = get_s(json_data,prov)
        return jsonify(pr)
    else:
        return jsonify({'Message':'0'})


@app.route('/sum')
def sum():
    provs=Cartix_population.query.with_entities(func.sum(Cartix_population.ctxpp_total))
    #grand_total = db.session.query(func.sum(models.Blogs.IMAGE_COUNT)).filter(models.Blogs.STATUS == 'A').scalar()

    if provs :
        result=ctxpps_schema.dump(provs)
        return jsonify({'Message':'1','Province Population':result.data})
    else:
        return jsonify({'Message':'0'})
