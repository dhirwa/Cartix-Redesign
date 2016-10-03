from marshmallow import Schema,fields


class Cartix_provinceSchema(Schema):
    ctxp_id = fields.Integer(dump_only = True)
    ctxp_name = fields.String()

ctxp_schema = Cartix_provinceSchema()
ctxps_schema = Cartix_provinceSchema(many = true)

class Cartix_districtSchema(Schema):
    ctxd_id = fields.Integer(dump_only = True)
    ctxd_name = fields.String()
    ctxp_pid= fields.Integer()

ctxd_schema = Cartix_districtSchema()
ctxds_schema = Cartix_districtSchema(many=True)

class Cartix_sectorSchema(Schema):
    ctxs_id = fields.Integer(dump_only = True)
    ctxs_name = fields.String()
    ctxd_did = fields.Integer()

ctxs_schema = Cartix_sectorSchema()
ctxss_schema = Cartix_sectorSchema(many = True)

class Cartix_savinggroupSchema(Schema):
    ctxsg_id= fields.Integer(dump_only = True)
    ctxsg_name= fields.String()
    ctxsg_creationyear= fields.Integer()
    ctxsg_sector= fields.Integer()
    ctxsg_district= fields.Integer()
    ctxsg_province= fields.Integer()
    ctxsg_members=fields.Integer()
    ctxsg_female=fields.Integer()
    ctxsg_male=fields.Integer()
    ctxsg_fundingNgo = fields.String()
    ctxsg_partnerNgo = fields.String()
    ctxsg_amount= fields.Integer()
    ctxsg_outstLoan= fields.Integer()

ctxsg_schema=Cartix_savinggroupSchema()
ctxgss_schema=Cartix_savinggroupSchema(many=True)



class Cartix_financialInstSchema(Schema):
    ctxfn_id= fields.Integer(dump_only = True)
    ctxfn_name=fields.String()
    ctxfn_type=fields.String()
    ctxfn_province=fields.Integer()
    ctxfn_district=fields.Integer()
    ctxfn_sector=fields.Integer()

ctxfn_schema=Cartix_financialInstSchema()
ctxfns_schema=Cartix_financialInstSchema(many=True)

class Cartix_agentSchema(Schema):
    ctxa_id = fields.Integer(dump_only = True)
    ctxa_name = fields.String()
    ctxa_type = fields.String()
    ctxa_province=fields.Integer()
    ctxa_district=fields.Integer()
    ctxa_sector=fields.Integer()

ctxa_schema=Cartix_agentSchema()
ctxas_schema=Cartix_agentSchema(many=True)

class Cartix_populationSchema(Schema):
    ctxpp_id=fields.Integer(dump_only = True)
    ctxpp_name=fields.String()
    ctxpp_total=fields.Integer()
    ctxpp_male=fields.Integer()
    ctxpp_female=fields.Integer()
    ctxpp_province=fields.Integer()
    ctxpp_district=fields.Integer()
    ctxpp_sector=fields.Integer()


ctxpp_schema=Cartix_populationSchema()
ctxpps_schema=Cartix_populationSchema(many=True)
