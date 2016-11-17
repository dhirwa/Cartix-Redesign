from xlrd import open_workbook
from flask import jsonify,request
import sqlite3 as sql
from flask import Flask
import psycopg2



app=Flask(__name__)



class Arm(object):
    def __init__(self, ctxs_id,ctxs_name,ctxs_district):
        self.ctxs_id = ctxs_id
        self.ctxs_name = ctxs_name
        self.ctxs_district = ctxs_district

    def __str__(self):
        return("  sect_id = {0}\n"
               "  sect_name = {1}\n"
               "  sect_distr = {2}\n"
               .format(self.ctxs_id, self.ctxs_name,self.ctxs_district))

wb = open_workbook('ctxss.xls')
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
        q='INSERT INTO cartix_sector(ctxs_id,ctxs_name,ctxs_district) VALUES (%s,%s,%s);'
        data=(item.ctxs_id,item.ctxs_name,item.ctxs_district)
        cur.execute(q,data)
        #cur.execute('INSERT INTO ctxp(ctxp_id,ctxp_name) VALUES (?,?)',(item.ctxp_id,item.ctxp_name))
        con.commit()

for item in items:
    print item

#    print("Accessing one single value (eg. Prov_name): {0}".format(item.ctxp_name))
#    print
