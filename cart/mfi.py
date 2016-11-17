from xlrd import open_workbook
from flask import jsonify,request
import sqlite3 as sql
from flask import Flask
import psycopg2



app=Flask(__name__)



class Arm(object):
    def __init__(self, ctxm_id,ctxm_province,ctxm_district,ctxm_sector,ctxm_name,ctxm_count):
        self.ctxm_id = ctxm_id
        self.ctxm_province = ctxm_province
        self.ctxm_district = ctxm_district
        self.ctxm_sector = ctxm_sector
        self.ctxm_name = ctxm_name
        self.ctxm_count = ctxm_count

    def __str__(self):
        return("  mfi_id = {0}\n"
               "  mfi_prov = {1}\n"
               "  mfi_dis = {2}\n"
               "  mfi_sect = {3}\n"
               "  mfi_name = {4}\n"
               "  mfi_count = {5}\n"
               .format(self.ctxm_id,self.ctxm_province,self.ctxm_district,self.ctxm_sector,self.ctxm_name,self.ctxm_count))

wb = open_workbook('mfi.xls')
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
        q='INSERT INTO cartix_mfi(ctxm_id,ctxm_province,ctxm_district,ctxm_sector,ctxm_name,ctxm_count) VALUES (%s,%s,%s,%s,%s,%s);'
        data=(item.ctxm_id,item.ctxm_province,item.ctxm_district,item.ctxm_sector,item.ctxm_name,item.ctxm_count)
        cur.execute(q,data)
        #cur.execute('INSERT INTO ctxp(ctxp_id,ctxp_name) VALUES (?,?)',(item.ctxp_id,item.ctxp_name))
        con.commit()

for item in items:
    print item

#    print("Accessing one single value (eg. Prov_name): {0}".format(item.ctxp_name))
#    print
