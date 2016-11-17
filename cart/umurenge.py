from xlrd import open_workbook
from flask import jsonify,request
import sqlite3 as sql
from flask import Flask
import psycopg2



app=Flask(__name__)



class Arm(object):
    def __init__(self, ctxsc_id,ctxsc_province,ctxsc_district,ctxsc_sector,ctxsc_name):
        self.ctxsc_id = ctxsc_id
        self.ctxsc_province = ctxsc_province
        self.ctxsc_district = ctxsc_district
        self.ctxsc_sector = ctxsc_sector
        self.ctxsc_name = ctxsc_name

    def __str__(self):
        return("  us_id = {0}\n"
               "  us_prov = {1}\n"
               "  us_dis = {2}\n"
               "  us_sect = {3}\n"
               "  us_name = {4}\n"
               .format(self.ctxsc_id,self.ctxsc_province,self.ctxsc_district,self.ctxsc_sector,self.ctxsc_name))

wb = open_workbook('umurenge.xls')
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
        q='INSERT INTO cartix_sacco(ctxsc_id,ctxsc_province,ctxsc_district,ctxsc_sector,ctxsc_name) VALUES (%s,%s,%s,%s,%s);'
        data=(item.ctxsc_id,item.ctxsc_province,item.ctxsc_district,item.ctxsc_sector,item.ctxsc_name)
        cur.execute(q,data)
        #cur.execute('INSERT INTO ctxp(ctxp_id,ctxp_name) VALUES (?,?)',(item.ctxp_id,item.ctxp_name))
        con.commit()

for item in items:
    print item

#    print("Accessing one single value (eg. Prov_name): {0}".format(item.ctxp_name))
#    print
