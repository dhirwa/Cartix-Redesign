from app.model.model import *
from app.model.schema import *


def get_province(json_data):

    prov=Cartix_province.query.get(json_data)
    if prov is None:
        pro=0
    else:
        pro=1

    return pro

def get_district(json_data):

    prov=Cartix_district.query.get(json_data)
    if prov is None:
        pro=0
    else:
        pro=1

    return pro

def get_sum(json_data,prov):
    output={'District Population':[]}
    dd=0
    cd=0
    bd=0

    for item in json_data:
        dd+=int(item['ctxpp_male'])
        cd+=int(item['ctxpp_female'])
        bd+=int(item['ctxpp_total'])

    data = {'district':prov,'female':cd,'male':dd,'total':bd}

    output['District Population'].append(data)
    return output,prov

def get_s(json_data,dis):
    output={'Province Population':[]}
    dd=0
    cd=0
    bd=0

    for item in json_data:
        dd+=int(item['ctxpp_male'])
        cd+=int(item['ctxpp_female'])
        bd+=int(item['ctxpp_total'])

    data = {'province':dis,'female':cd,'male':dd,'total':bd}

    output['Province Population'].append(data)
    return output,dis
