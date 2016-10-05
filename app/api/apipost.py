from app.model.model import *
from app.model.schema import *
from app.controllers.controller import *
from flask import jsonify,request
import datetime
import base64
import os


@app.route('/provinces/',methods=['POST'])
def prov():
    json_data = request.get_json()
    if not json_data:
        return jsonify({'Message':'No input data provided'})
    data,errors=ctxp_schema.load(json_data)
    if errors:
        return jsonify(errors), 422
    ctxp_name=data['ctxp_name']
    ctx = Cartix_province.query.filter_by(ctxp_name=ctxp_name).first()
    if ctx is None:
        ctxp_prov=Cartix_province(
            ctxp_name=data["ctxp_name"]
        )
        db.session.add(ctxp_prov)
        db.session.commit()
        result=ctxp_schema.dump(Cartix_province.query.get(ctxp_prov.ctxp_id))
        return jsonify({'Message':'1','Province':result.data})

    else:
        return jsonify({'Message':'Province already in'})

@app.route('/districts/',methods=['POST'])
def dist():
    json_data = request.get_json()
    if not json_data:
        return jsonify({'Message':'No input data provided'})
    data,errors=ctxd_schema.load(json_data)
    if errors:
        return jsonify(errors), 422
    ctxd_name=data['ctxd_name']
    prov = get_province(data['ctxd_province'])
    if prov==1:

        ctx = Cartix_district.query.filter_by(ctxd_name=ctxd_name).first()
        if ctx is None:
            ctxp_dist=Cartix_district(
                ctxd_name=data["ctxd_name"],
                ctxd_province=data["ctxd_province"]
            )
            db.session.add(ctxp_dist)
            db.session.commit()
            result=ctxd_schema.dump(Cartix_district.query.get(ctxp_dist.ctxd_id))
            return jsonify({'Message':'1','District':result.data})

        else:
            return jsonify({'Message':'District already in'})
    else:
        return jsonify({'Message':'0'})


@app.route('/sectors/',methods=['POST'])
def sect():
    json_data = request.get_json()
    if not json_data:
        return jsonify({'Message':'No input data provided'})
    data,errors=ctxs_schema.load(json_data)
    if errors:
        return jsonify(errors), 422

    ctxs_name = data['ctxs_name']
    prov = get_district(data['ctxs_district'])
    if prov==1:
        ctxp_sect=Cartix_sector(
            ctxs_name=data["ctxs_name"],
            ctxs_district=data["ctxs_district"]
        )
        db.session.add(ctxp_sect)
        db.session.commit()
        result=ctxs_schema.dump(Cartix_sector.query.get(ctxp_sect.ctxs_id))
        return jsonify({'Message':'1','Sector':result.data})
    else:
        return jsonify({'Message':'0'})

@app.route('/population/',methods=['POST'])
def pop():
    json_data = request.get_json()
    if not json_data:
        return jsonify({'Message':'No input data provided'})
    data,errors=ctxpp_schema.load(json_data)
    if errors:
        return jsonify(errors), 422

    ct = data['ctxpp_sector']
    ctx = Cartix_population.query.filter_by(ctxpp_sector = ct).first()

    if ctx is None:
        ctxp_pop=Cartix_population(
            ctxpp_total=data['ctxpp_total'],
            ctxpp_male=data['ctxpp_male'],
            ctxpp_female=data['ctxpp_female'],
            ctxpp_sector=data['ctxpp_sector'],
            ctxpp_district=data['ctxpp_district'],
            ctxpp_province=data['ctxpp_province']
        )
        db.session.add(ctxp_pop)
        db.session.commit()
        result=ctxpp_schema.dump(Cartix_population.query.get(ctxp_pop.ctxpp_id))
        return jsonify({'Message':'1','Population':result.data})
    else:
        return jsonify({'Message':'0'})
