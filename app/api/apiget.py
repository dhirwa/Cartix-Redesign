from app import *
from app.model.model import *
from app.model.schema import *
import datetime
from sqlalchemy import func
from app.controllers.controller import *


@app.errorhandler(404)
def page_not_found(e):
    return 'Error 404: Page not found, Please check ur route well.'

#=======================================================  ADMINISTRATIVE AREAS  ====================================================


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


#=====================================================  POPULATION  ===============================================================


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




#============================================== SAVINGGROUPS===================================================================




@app.route('/getsavinggroup')
def get_svg():
    svgs=Cartix_savinggroup.query.all()
    result=ctxsgs_schema.dump(svgs)
    return jsonify({'Saving groups':result.data})

@app.route('/getsavinggroup/district/<int:dist>')
def get_svgdis(dist):
    d=Cartix_savinggroup.query.filter_by(ctxsg_district=dist).all()
    if d is None:
       return jsonify({'Message':'0'})
    else:
    	res = ctxsgs_schema.dump(d)
    	return jsonify(res)

@app.route('/getsavinggroups/number/dist/<int:dist>')
def get_savnd(dist):
    provs=Cartix_savinggroup.query.filter_by(ctxsg_district=dist).all()
    json_data = ctxsgs_schema.dump(provs).data
    pr,provs = get_svgd(json_data,provs)
    return jsonify(pr)

@app.route('/getsavinggroups/number/prov/<int:prov>')
def get_savp(prov):
    provs=Cartix_savinggroup.query.filter_by(ctxsg_province=prov).all()
    json_data = ctxsgs_schema.dump(provs).data
    pr,provs = get_svgp(json_data,provs)
    return jsonify(pr)


@app.route('/getsavinggroups/number/sect/<int:sect>')
def get_savs(sect):
    provs=Cartix_savinggroup.query.filter_by(ctxsg_sector=sect).all()
    json_data = ctxsgs_schema.dump(provs).data
    pr,provs = get_svgs(json_data,provs)
    return jsonify(pr)


@app.route('/getsavinggroups/dist/<int:dist>/<name>')
def get_savsn(dist,name):
    provs=Cartix_savinggroup.query.filter_by(ctxsg_district=dist).filter_by(ctxsg_fundingngo=name).all()
    json_data = ctxsgs_schema.dump(provs).data
    pr,provs = get_svgsn(json_data,provs)
    return jsonify(pr)

@app.route('/getsavinggroups/sect/<int:sect>/<name>')
def get_savss(sect,name):
    provs=Cartix_savinggroup.query.filter_by(ctxsg_sector=sect).filter_by(ctxsg_fundingngo=name).all()
    json_data = ctxsgs_schema.dump(provs).data
    pr,provs = get_svgsn(json_data,provs)
    return jsonify(pr)

@app.route('/getsavinggroups/prov/<int:dist>/<name>')
def get_savsp(dist,name):
    provs=Cartix_savinggroup.query.filter_by(ctxsg_province=dist).filter_by(ctxsg_fundingngo=name).all()
    json_data = ctxsgs_schema.dump(provs).data
    pr,provs = get_svgsn(json_data,provs)
    return jsonify(pr)


#====================================================== AGENTS =====================================================================
@app.route('/getagents')
def get_Ag():
    provs=Cartix_telcoagent.query.all()
    result=ctxas_schema.dump(provs)
    return jsonify({'Agents':result.data})

@app.route('/gettagents/province/<int:pid>')
def get_agpr(pid):
    provs=Cartix_telcoagent.query.filter_by(ctxa_province=pid).all()
    json_data = ctxas_schema.dump(provs).data
    pr= get_agp(json_data)
    return jsonify(pr)

@app.route('/gettagents/district/<int:pid>')
def get_agdi(pid):
    provs=Cartix_telcoagent.query.filter_by(ctxa_district=pid).all()
    json_data = ctxas_schema.dump(provs).data
    pr = get_agp(json_data)
    return jsonify(pr)

@app.route('/getbagents/province/<int:pid>')
def get_agbpr(pid):
    provs=Cartix_bankagent.query.filter_by(ctxba_province=pid).all()
    json_data = ctxbas_schema.dump(provs).data
    pr = get_agp(json_data)
    return jsonify(pr)

@app.route('/getbagents/district/<int:pid>')
def get_agbdi(pid):
    provs=Cartix_bankagent.query.filter_by(ctxba_district=pid).all()
    json_data = ctxbas_schema.dump(provs).data
    pr = get_agp(json_data)
    return jsonify(pr)

@app.route('/getallagents/province/<int:pid>')
def get_agala(pid):
    provs=Cartix_telcoagent.query.filter_by(ctxa_province=pid).all()
    provd=Cartix_bankagent.query.filter_by(ctxba_province=pid).all()
    json_data = ctxas_schema.dump(provs).data
    json_d=ctxbas_schema.dump(provd).data
    pr,p,provs = get_agallp(json_data,json_d,provs)
    return jsonify(pr)

@app.route('/getallagents/district/<int:pid>')
def get_agalad(pid):
    provs=Cartix_telcoagent.query.filter_by(ctxa_district=pid).all()
    provd=Cartix_bankagent.query.filter_by(ctxba_district=pid).all()
    json_data = ctxas_schema.dump(provs).data
    json_d=ctxbas_schema.dump(provd).data
    pr,p,provs = get_agallp(json_data,json_d,provs)
    return jsonify(pr)

#======================================================== FINANCIAL INSTITUTIONS ===================================================

@app.route('/getsacco')
def get_sacco():
    provs=Cartix_sacco.query.all()
    result=ctxscs_schema.dump(provs)
    return jsonify({'Saccos':result})

@app.route('/getsacco/province/<int:pid>')
def get_saccop(pid):
    provs=Cartix_sacco.query.filter_by(ctxsc_province=pid).all()
    json_data=ctxscs_schema.dump(provs).data
    pr=get_sacp(json_data)
    return jsonify(pr)

@app.route('/getsacco/district/<int:pid>')
def get_saccod(pid):
    provs=Cartix_sacco.query.filter_by(ctxsc_district=pid).all()
    json_data=ctxscs_schema.dump(provs).data
    pr=get_sacp(json_data)
    return jsonify(pr)

@app.route('/getsacco/sector/<int:pid>')
def get_saccos(pid):
    provs=Cartix_sacco.query.filter_by(ctxsc_sector=pid).all()
    json_data=ctxscs_schema.dump(provs).data
    pr=get_sacp(json_data)
    return jsonify(pr)

@app.route('/getnonsacco')
def get_nonsacco():
    provs=Cartix_nonsacco.query.all()
    result=ctxnus_schema.dump(provs)
    return jsonify({'Non_Saccos':result})

@app.route('/getnonsacco/province/<int:pid>')
def get_nonsaccop(pid):
    provs=Cartix_nonsacco.query.filter_by(ctxnu_province=pid).all()
    json_data=ctxnus_schema.dump(provs).data
    pr=get_nonsacp(json_data)
    return jsonify(pr)

@app.route('/getnonsacco/district/<int:pid>')
def get_nonsaccod(pid):
    provs=Cartix_nonsacco.query.filter_by(ctxnu_district=pid).all()
    json_data=ctxnus_schema.dump(provs).data
    pr=get_nonsacp(json_data)
    return jsonify(pr)

@app.route('/getnonsacco/sector/<int:pid>')
def get_nonsaccos(pid):
    provs=Cartix_nonsacco.query.filter_by(ctxnu_sector=pid).all()
    json_data=ctxnus_schema.dump(provs).data
    pr=get_nonsacp(json_data)
    return jsonify(pr)

@app.route('/getmfi/province/<int:pid>')
def get_mfi(pid):
    provs=Cartix_mfi.query.filter_by(ctxm_province=pid).all()
    json_data=ctxms_schema.dump(provs).data
    pr=get_mfip(json_data)
    return jsonify(pr)

@app.route('/getmfi/district/<int:pid>')
def get_mfid(pid):
    provs=Cartix_mfi.query.filter_by(ctxm_district=pid).all()
    json_data=ctxms_schema.dump(provs).data
    pr=get_mfip(json_data)
    return jsonify(pr)

@app.route('/getmfi/sector/<int:pid>')
def get_mfis(pid):
    provs=Cartix_mfi.query.filter_by(ctxm_sector=pid).all()
    json_data=ctxms_schema.dump(provs).data
    pr=get_mfip(json_data)
    return jsonify(pr)

@app.route('/getbanks/province/<int:pid>')
def get_bk(pid):
    provs=Cartix_bank.query.filter_by(ctxb_province=pid).all()
    json_data=ctxbs_schema.dump(provs).data
    pr=get_bkp(json_data)
    return jsonify(pr)

@app.route('/getbanks/district/<int:pid>')
def get_bkd(pid):
    provs=Cartix_bank.query.filter_by(ctxb_district=pid).all()
    json_data=ctxbs_schema.dump(provs).data
    pr=get_bkp(json_data)
    return jsonify(pr)

@app.route('/getbanks/sector/<int:pid>')
def get_bks(pid):
    provs=Cartix_bank.query.filter_by(ctxb_sector=pid).all()
    json_data=ctxbs_schema.dump(provs).data
    pr=get_bkp(json_data)
    return jsonify(pr)


#================================================================  GROUPING  =======================================================

@app.route('/getall/province/<int:pid>')
def get_all(pid):
    provs=Cartix_savinggroup.query.filter_by(ctxsg_province=pid).all()
    provm=Cartix_mfi.query.filter_by(ctxm_province=pid).all()
    provb=Cartix_bank.query.filter_by(ctxb_province=pid).all()
    provsc=Cartix_sacco.query.filter_by(ctxsc_province=pid).all()
    provnu=Cartix_nonsacco.query.filter_by(ctxnu_province=pid).all()
    provp=Cartix_population.query.filter_by(ctxpp_province=pid).all()
    prova=Cartix_telcoagent.query.filter_by(ctxa_province=pid).all()
    provba=Cartix_bankagent.query.filter_by(ctxba_province=pid).all()
    json_ds=ctxsgs_schema.dump(provs).data
    json_dm=ctxms_schema.dump(provm).data
    json_db=ctxbs_schema.dump(provb).data
    json_dsc=ctxscs_schema.dump(provsc).data
    json_dnu=ctxnus_schema.dump(provnu).data
    json_dp=ctxpps_schema.dump(provp).data
    json_da=ctxas_schema.dump(prova).data
    json_dba=ctxbas_schema.dump(provba).data
    pr=get_sh(json_ds,json_dm,json_db,json_dsc,json_dnu,json_dp,json_da,json_dba)
    return jsonify(pr)

@app.route('/getall/district/<int:pid>')
def get_alld(pid):
    provs=Cartix_savinggroup.query.filter_by(ctxsg_district=pid).all()
    provm=Cartix_mfi.query.filter_by(ctxm_district=pid).all()
    provb=Cartix_bank.query.filter_by(ctxb_district=pid).all()
    provsc=Cartix_sacco.query.filter_by(ctxsc_district=pid).all()
    provnu=Cartix_nonsacco.query.filter_by(ctxnu_district=pid).all()
    provp=Cartix_population.query.filter_by(ctxpp_district=pid).all()
    prova=Cartix_telcoagent.query.filter_by(ctxa_district=pid).all()
    provba=Cartix_bankagent.query.filter_by(ctxba_district=pid).all()
    json_ds=ctxsgs_schema.dump(provs).data
    json_dm=ctxms_schema.dump(provm).data
    json_db=ctxbs_schema.dump(provb).data
    json_dsc=ctxscs_schema.dump(provsc).data
    json_dnu=ctxnus_schema.dump(provnu).data
    json_dp=ctxpps_schema.dump(provp).data
    json_da=ctxas_schema.dump(prova).data
    json_dba=ctxbas_schema.dump(provba).data
    pr=get_sh(json_ds,json_dm,json_db,json_dsc,json_dnu,json_dp,json_da,json_dba)
    return jsonify(pr)

@app.route('/getall/sector/<int:pid>')
def get_alls(pid):
    provs=Cartix_savinggroup.query.filter_by(ctxsg_sector=pid).all()
    provm=Cartix_mfi.query.filter_by(ctxm_sector=pid).all()
    provb=Cartix_bank.query.filter_by(ctxb_sector=pid).all()
    provsc=Cartix_sacco.query.filter_by(ctxsc_sector=pid).all()
    provnu=Cartix_nonsacco.query.filter_by(ctxnu_sector=pid).all()
    provp=Cartix_population.query.filter_by(ctxpp_sector=pid).all()
    json_ds=ctxsgs_schema.dump(provs).data
    json_dm=ctxms_schema.dump(provm).data
    json_db=ctxbs_schema.dump(provb).data
    json_dsc=ctxscs_schema.dump(provsc).data
    json_dnu=ctxnus_schema.dump(provnu).data
    json_dp=ctxpps_schema.dump(provp).data
    pr=get_shs(json_ds,json_dm,json_db,json_dsc,json_dnu,json_dp)
    return jsonify(pr)
