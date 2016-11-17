from xlrd import open_workbook
from flask import jsonify,request
import sqlite3 as sql
from flask import Flask
import psycopg2



app=Flask(__name__)



class Arm(object):
    def __init__(self, ctxa_id,ctxa_count,ctxa_district,ctxa_province):
        self.ctxa_id = ctxa_id
        self.ctxa_count = ctxa_count
        self.ctxa_district = ctxa_district
        self.ctxa_province = ctxa_province

    def __str__(self):
        return("  telco_id = {0}\n"
               "  telco_count = {1}\n"
               "  telco_dist = {2}\n"
               "  telco_prov = {3}\n"
               .format(self.ctxa_id,self.ctxa_count,self.ctxa_district,self.ctxa_province))

wb = open_workbook('telco.xls')
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
        q='INSERT INTO cartix_telcoagent(ctxa_id,ctxa_count,ctxa_district,ctxa_province) VALUES (%s,%s,%s,%s);'
        data=(item.ctxa_id,item.ctxa_count,item.ctxa_district,item.ctxa_province)
        cur.execute(q,data)
        #cur.execute('INSERT INTO ctxp(ctxp_id,ctxp_name) VALUES (?,?)',(item.ctxp_id,item.ctxp_name))
        con.commit()

for item in items:
    print item

#    print("Accessing one single value (eg. Prov_name): {0}".format(item.ctxp_name))
#    print
