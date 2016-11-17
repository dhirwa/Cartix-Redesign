from xlrd import open_workbook
from flask import jsonify,request
import sqlite3 as sql
from flask import Flask
import psycopg2



app=Flask(__name__)



class Arm(object):
    def __init__(self, ctxsg_id,ctxsg_name,ctxsg_creationyear,ctxsg_sector,ctxsg_district,ctxsg_province,ctxsg_members,ctxsg_female,ctxsg_male,ctxsg_fundingngo,ctxsg_partnerngo,ctxsg_amount,ctxsg_outstloan,ctxsg_status):
        self.ctxsg_id = ctxsg_id
        self.ctxsg_name = ctxsg_name
        self.ctxsg_creationyear = ctxsg_creationyear
        self.ctxsg_sector = ctxsg_sector
        self.ctxsg_district = ctxsg_district
        self.ctxsg_province = ctxsg_province
        self.ctxsg_members = ctxsg_members
        self.ctxsg_female = ctxsg_female
        self.ctxsg_male = ctxsg_male
        self.ctxsg_fundingngo = ctxsg_fundingngo
        self.ctxsg_partnerngo = ctxsg_partnerngo
        self.ctxsg_amount = ctxsg_amount
        self.ctxsg_outstloan = ctxsg_outstloan
        self.ctxsg_status = ctxsg_status
    def __str__(self):
        return("  sg_id = {0}\n"
               "  sg_name = {1}\n"
               "  sg_cy = {2}\n"
               "  sg_sect = {3}\n"
               "  sg_dist = {4}\n"
               "  sg_prov = {5}\n"
               "  sg_memb = {6}\n"
               "  sg_fem = {7}\n"
               "  sg_mal = {8}\n"
               "  sg_fn = {9}\n"
               "  sg_pn = {10}\n"
               "  sg_amount = {11}\n"
               "  sg_outst = {12}\n"
               "  sg_status = {13}\n"
               .format(self.ctxsg_id, self.ctxsg_name,self.ctxsg_creationyear,self.ctxsg_sector,self.ctxsg_district,self.ctxsg_province,self.ctxsg_members,self.ctxsg_female,self.ctxsg_male,self.ctxsg_fundingngo,self.ctxsg_partnerngo,self.ctxsg_amount,self.ctxsg_outstloan,self.ctxsg_status))

wb = open_workbook('svgL.xls')
for sheet in wb.sheets():
    number_of_rows = sheet.nrows
    number_of_columns = sheet.ncols

    items = []

    rows = []
    for row in range(1, number_of_rows):
        values = []
        for col in range(number_of_columns):
            value  = (sheet.cell(row,col).value)
            try:
                value = str(int(value))

            except ValueError:
                pass
            finally:
                values.append(value)


        item = Arm(*values)
        items.append(item)
    #with sql.connect('gigi.db') as con:
    con = psycopg2.connect(database="cartix", user="postgres", password="password", host="127.0.0.1", port="5432")
    cur=con.cursor()
    for item in items:
        q='INSERT INTO cartix_savinggroup(ctxsg_id,ctxsg_name,ctxsg_creationyear,ctxsg_sector,ctxsg_district,ctxsg_province,ctxsg_members,ctxsg_female,ctxsg_male,ctxsg_fundingngo,ctxsg_partnerngo,ctxsg_amount,ctxsg_outstloan,ctxsg_status) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);'
        data=(item.ctxsg_id,item.ctxsg_name,item.ctxsg_creationyear,item.ctxsg_sector,item.ctxsg_district,item.ctxsg_province,item.ctxsg_members,item.ctxsg_female,item.ctxsg_male,item.ctxsg_fundingngo,item.ctxsg_partnerngo,item.ctxsg_amount,item.ctxsg_outstloan,item.ctxsg_status)
        cur.execute(q,data)
        #cur.execute('INSERT INTO ctxp(ctxp_id,ctxp_name) VALUES (?,?)',(item.ctxp_id,item.ctxp_name))
        con.commit()

for item in items:
    print item

#    print("Accessing one single value (eg. Prov_name): {0}".format(item.ctxp_name))
#    print
