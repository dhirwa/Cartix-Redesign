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
    ctxsg_members=fields.Integer()
    ctxsg_female=fields.Integer()
    ctxsg_male=fields.Integer()
    ctxsg_fundingNgo = fields.String()
    ctxsg_partnerNgo = fields.String()
    ctxsg_amount= fields.Decimal()
    ctxsg_outstLoan= fields.Decimal()

ctxsg_schema=Cartix_savinggroupSchema()
ctxgss_schema=Cartix_savinggroupSchema(many=True)
