from xlrd import open_workbook
from flask import jsonify,request
import sqlite3 as sql
from flask import Flask
import psycopg2



app=Flask(__name__)



class Arm(object):
    def __init__(self, ctxnu_id,ctxnu_province,ctxnu_district,ctxnu_sector,ctxnu_name):
        self.ctxnu_id = ctxnu_id
        self.ctxnu_province = ctxnu_province
        self.ctxnu_district = ctxnu_district
        self.ctxnu_sector = ctxnu_sector
        self.ctxnu_name = ctxnu_name

    def __str__(self):
        return("  nonu_id = {0}\n"
               "  nonu_prov = {1}\n"
               "  nonu_dis = {2}\n"
               "  nonu_sect = {3}\n"
               "  nonu_name = {4}\n"
               .format(self.ctxnu_id,self.ctxnu_province,self.ctxnu_district,self.ctxnu_sector,self.ctxnu_name))

wb = open_workbook('nonumurenge.xls')
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
        q='INSERT INTO cartix_nonsacco(ctxnu_id,ctxnu_province,ctxnu_district,ctxnu_sector,ctxnu_name) VALUES (%s,%s,%s,%s,%s);'
        data=(item.ctxnu_id,item.ctxnu_province,item.ctxnu_district,item.ctxnu_sector,item.ctxnu_name)
        cur.execute(q,data)
        #cur.execute('INSERT INTO ctxp(ctxp_id,ctxp_name) VALUES (?,?)',(item.ctxp_id,item.ctxp_name))
        con.commit()

for item in items:
    print item

#    print("Accessing one single value (eg. Prov_name): {0}".format(item.ctxp_name))
#    print
