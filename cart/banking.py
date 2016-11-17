from xlrd import open_workbook
from flask import jsonify,request
import sqlite3 as sql
from flask import Flask
import psycopg2



app=Flask(__name__)



class Arm(object):
    def __init__(self, ctxb_id,ctxb_province,ctxb_district,ctxb_sector,ctxb_name,ctxb_branches):
        self.ctxb_id = ctxb_id
        self.ctxb_province = ctxb_province
        self.ctxb_district = ctxb_district
        self.ctxb_sector = ctxb_sector
        self.ctxb_name = ctxb_name
        self.ctxb_branches = ctxb_branches

    def __str__(self):
        return("  bank_id = {0}\n"
               "  bank_prov = {1}\n"
               "  bank_dis = {2}\n"
               "  bank_sect = {3}\n"
               "  bank_name = {4}\n"
               "  bank_branches = {5}\n"
               .format(self.ctxb_id,self.ctxb_province,self.ctxb_district,self.ctxb_sector,self.ctxb_name,self.ctxb_branches))

wb = open_workbook('listbb.xls')
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
        q='INSERT INTO cartix_bank(ctxb_id,ctxb_province,ctxb_district,ctxb_sector,ctxb_name,ctxb_branches) VALUES (%s,%s,%s,%s,%s,%s);'
        data=(item.ctxb_id,item.ctxb_province,item.ctxb_district,item.ctxb_sector,item.ctxb_name,item.ctxb_branches)
        cur.execute(q,data)
        #cur.execute('INSERT INTO ctxp(ctxp_id,ctxp_name) VALUES (?,?)',(item.ctxp_id,item.ctxp_name))
        con.commit()

for item in items:
    print item

#    print("Accessing one single value (eg. Prov_name): {0}".format(item.ctxp_name))
#    print
