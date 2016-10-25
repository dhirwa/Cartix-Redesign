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


def get_svgd(json_data,prov):
    output={'District Savinggroups':[]}
    d=0
    c=0
    b=0
    a=0
    for item in json_data:
        d+=1
        c+=int(item['ctxsg_members'])
        b+=int(item['ctxsg_amount'])
        a+=int(item['ctxsg_outstloan'])
    data = {'SGs_count':d,'SGs_membership':c,'SGs_amount':b,'SGs_outstLoan':a}
    output['District Savinggroups'].append(data)
    return output,prov

def get_svgp(json_data,prov):
    output={'Province Savinggroups':[]}
    d=0
    c=0
    b=0
    a=0

    for item in json_data:
        d+=1
        c+=int(item['ctxsg_members'])
        b+=int(item['ctxsg_amount'])
        a+=int(item['ctxsg_outstloan'])
    data = {'SGs_count':d,'SGs_membership':c,'SGs_amount':b,'SGs_outstLoan':a}
    output['Province Savinggroups'].append(data)
    return output,prov

def get_svgs(json_data,prov):
    output={'Sector Savinggroups':[]}
    d=0
    c=0
    b=0
    a=0

    for item in json_data:
        d+=1
        c+=int(item['ctxsg_members'])
        b+=int(item['ctxsg_amount'])
        a+=int(item['ctxsg_outstloan'])
    data = {'SGs_count':d,'SGs_membership':c,'SGs_amount':b,'SGs_outstLoan':a}
    output['Sector Savinggroups'].append(data)
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
