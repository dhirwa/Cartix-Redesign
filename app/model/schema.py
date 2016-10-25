from marshmallow import Schema,fields


class Cartix_provinceSchema(Schema):
    ctxp_id = fields.Integer(dump_only = True)
    ctxp_name = fields.String()

ctxp_schema = Cartix_provinceSchema()
ctxps_schema = Cartix_provinceSchema(many = True)

class Cartix_districtSchema(Schema):
    ctxd_id = fields.Integer(dump_only = True)
    ctxd_name = fields.String()
    ctxd_province= fields.Integer()

ctxd_schema = Cartix_districtSchema()
ctxds_schema = Cartix_districtSchema(many=True)

class Cartix_sectorSchema(Schema):
    ctxs_id = fields.Integer(dump_only = True)
    ctxs_name = fields.String()
    ctxs_district = fields.Integer()

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
    ctxsg_fundingngo = fields.String()
    ctxsg_partnerngo = fields.String()
    ctxsg_status = fields.String()
    ctxsg_amount= fields.Float()
    ctxsg_outstloan= fields.Float()

ctxsg_schema=Cartix_savinggroupSchema()
ctxsgs_schema=Cartix_savinggroupSchema(many=True)



class Cartix_bankSchema(Schema):
    ctxb_id=fields.Integer()
    ctxb_province=fields.Integer()
    ctxb_district=fields.Integer()
    ctxb_sector=fields.Integer()
    ctxb_name=fields.String()
    ctxb_branches=fields.String()

ctxb_schema=Cartix_bankSchema()
ctxbs_schema=Cartix_bankSchema(many=True)

class Cartix_mfiSchema(Schema):
    ctxm_id=fields.Integer()
    ctxm_province=fields.Integer()
    ctxm_district=fields.Integer()
    ctxm_sector=fields.Integer()
    ctxm_name=fields.String()
    ctxm_count=fields.Integer()

ctxm_schema=Cartix_mfiSchema()
ctxms_schema=Cartix_mfiSchema(many=True)

class Cartix_nonsaccoSchema(Schema):
    ctxnu_id=fields.Integer()
    ctxnu_province=fields.Integer()
    ctxnu_district=fields.Integer()
    ctxnu_sector=fields.Integer()
    ctxnu_name=fields.String()

ctxnu_schema=Cartix_nonsaccoSchema()
ctxnus_schema=Cartix_nonsaccoSchema(many=True)

class Cartix_saccoSchema(Schema):
    ctxsc_id=fields.Integer()
    ctxsc_province=fields.Integer()
    ctxsc_district=fields.Integer()
    ctxsc_sector=fields.Integer()
    ctxsc_name=fields.String()

ctxsc_schema=Cartix_saccoSchema()
ctxscs_schema=Cartix_saccoSchema(many=True)


class Cartix_telcoagentSchema(Schema):
    ctxa_id = fields.Integer(dump_only = True)
    ctxa_province=fields.Integer()
    ctxa_district=fields.Integer()
    ctxa_count=fields.Integer()

ctxa_schema=Cartix_telcoagentSchema()
ctxas_schema=Cartix_telcoagentSchema(many=True)

class Cartix_bankagentSchema(Schema):
    ctxba_id = fields.Integer(dump_only = True)
    ctxba_province=fields.Integer()
    ctxba_district=fields.Integer()
    ctxba_count=fields.Integer()

ctxba_schema=Cartix_bankagentSchema()
ctxbas_schema=Cartix_bankagentSchema(many=True)


class Cartix_populationSchema(Schema):
    ctxpp_id=fields.Integer(dump_only = True)
    ctxpp_total=fields.Integer()
    ctxpp_male=fields.Integer()
    ctxpp_female=fields.Integer()
    ctxpp_province=fields.Integer()
    ctxpp_district=fields.Integer()
    ctxpp_sector=fields.Integer()


ctxpp_schema=Cartix_populationSchema()
ctxpps_schema=Cartix_populationSchema(many=True)
