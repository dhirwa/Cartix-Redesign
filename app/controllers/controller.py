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

def get_svgsn(json_data,prov):
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

def get_agp(json_data):
    output={'Agents':[]}
    d=0
    for item in json_data:
        d+=int(item['ctxa_count'])

    data = {'Ags_count':d}
    output['Agents'].append(data)
    return output

def get_agallp(json_data,json_d,prov):
    output={'Agents':[]}
    d=0
    c=0
    for item in json_data:
        d+=int(item['ctxa_count'])
    for item in json_d:
        c+=int(item['ctxba_count'])
    data = {'TelcoAgs_count':d,'BankAgs_count':c}
    output['Agents'].append(data)
    return output,json_d,prov

def get_bkp(json_data):
    output={'Banks':[]}
    d=0
    for item in json_data:
        d+=1
    data = {'Banks_count':d}
    output['Banks'].append(data)
    return output

def get_sacp(json_data):
    output={'Saccos':[]}
    d=0
    for item in json_data:
        d+=1
    data = {'Saccos_count':d}
    output['Saccos'].append(data)
    return output

def get_nonsacp(json_data):
    output={'Non_Saccos':[]}
    d=0
    for item in json_data:
        d+=1
    data = {'NonSaccos_count':d}
    output['Non_Saccos'].append(data)
    return output

def get_mfip(json_data):
    output={'Mfis':[]}
    d=0
    for item in json_data:
        d+=int(item['ctxm_count'])
    data = {'Mfi_count':d}
    output['Mfis'].append(data)
    return output

def get_bkp(json_data):
    output={'Banks':[]}
    d=0
    for item in json_data:
        d+=1
    data = {'Banks_count':d}
    output['Banks'].append(data)
    return output

def get_sh(json_ds,json_dm,json_db,json_dsc,json_dnu,json_dp,json_da,json_dba):
    output={'All':[]}
    a=0
    b=0
    c=0
    d=0
    e=0
    f=0
    g=0
    h=0
    i=0
    j=0
    for item in json_ds:
        a+=1
        j+=int(item['ctxsg_members'])
    for item in json_dm:
        b+=int(item['ctxm_count'])
    for item in json_db:
        c+=1
    for item in json_dsc:
        d+=1
    for item in json_dnu:
        e+=1
    for item in json_dp:
        f+=int(item['ctxpp_female'])
        g+=int(item['ctxpp_male'])
    for item in json_da:
        h+=int(item['ctxa_count'])
    for item in json_dba:
        i+=int(item['ctxba_count'])
    data= {'SGS_count':a,'SGs_membership':j,'Banks':c,'MFIs':b,'Umurenge Sacco':d,'Non_Umurenge Sacco':e,'TelcoAgents':h,'BankAgents':i,'Adult Female':f,'Adult Male':g}
    output['All'].append(data)
    return output

def get_shs(json_ds,json_dm,json_db,json_dsc,json_dnu,json_dp):
    output={'All':[]}
    a=0
    b=0
    c=0
    d=0
    e=0
    f=0
    g=0
    j=0
    for item in json_ds:
        a+=1
        j+=int(item['ctxsg_members'])
    for item in json_dm:
        b+=int(item['ctxm_count'])
    for item in json_db:
        c+=1
    for item in json_dsc:
        d+=1
    for item in json_dnu:
        e+=1
    for item in json_dp:
        f+=int(item['ctxpp_female'])
        g+=int(item['ctxpp_male'])
    data= {'SGS_count':a,'SGs_membership':j,'Banks':c,'MFIs':b,'Umurenge Sacco':d,'Non_Umurenge Sacco':e,'Adult Female':f,'Adult Male':g}
    output['All'].append(data)
    return output
