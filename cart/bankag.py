from xlrd import open_workbook
from flask import jsonify,request
import sqlite3 as sql
from flask import Flask
import psycopg2



app=Flask(__name__)



class Arm(object):
    def __init__(self, ctxba_id,ctxba_count,ctxba_district,ctxba_province):
        self.ctxba_id = ctxba_id
        self.ctxba_count = ctxba_id
        self.ctxba_district = ctxba_district
        self.ctxba_province = ctxba_province

    def __str__(self):
        return("  bank_id = {0}\n"
               "  bank_count = {1}\n"
               "  bank_dist = {2}\n"
               "  bank_prov = {3}\n"
               .format(self.ctxba_id,self.ctxba_count,self.ctxba_district,self.ctxba_province))

wb = open_workbook('banks.xls')
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
        q='INSERT INTO cartix_bankagent(ctxba_id,ctxba_count,ctxba_district,ctxba_province) VALUES (%s,%s,%s,%s);'
        data=(item.ctxba_id,item.ctxba_count,item.ctxba_district,item.ctxba_province)
        cur.execute(q,data)
        #cur.execute('INSERT INTO ctxp(ctxp_id,ctxp_name) VALUES (?,?)',(item.ctxp_id,item.ctxp_name))
        con.commit()

for item in items:
    print item

#    print("Accessing one single value (eg. Prov_name): {0}".format(item.ctxp_name))
#    print
