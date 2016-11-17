from xlrd import open_workbook
from flask import jsonify,request
import sqlite3 as sql
from flask import Flask
import psycopg2



app=Flask(__name__)



class Arm(object):
    def __init__(self, ctxd_id,ctxd_name,ctxd_province):
        self.ctxd_id = ctxd_id
        self.ctxd_name = ctxd_name
        self.ctxd_province = ctxd_province

    def __str__(self):
        return("  Distr_id = {0}\n"
               "  Distr_name = {1}\n"
               "  Distr_provi = {2}\n"
               .format(self.ctxd_id, self.ctxd_name,self.ctxd_province))

wb = open_workbook('ctxp.xls')
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
        q='INSERT INTO cartix_district(ctxd_id,ctxd_name,ctxd_province) VALUES (%s,%s,%s);'
        data=(item.ctxd_id,item.ctxd_name,item.ctxd_province)
        cur.execute(q,data)
        #cur.execute('INSERT INTO ctxp(ctxp_id,ctxp_name) VALUES (?,?)',(item.ctxp_id,item.ctxp_name))
        con.commit()

for item in items:
    print item

#    print("Accessing one single value (eg. Prov_name): {0}".format(item.ctxp_name))
#    print
