from xlrd import open_workbook
from flask import jsonify,request
import sqlite3 as sql
from flask import Flask
import psycopg2



app=Flask(__name__)



class Arm(object):
    def __init__(self, ctxpp_id,ctxpp_province,ctxpp_district,ctxpp_sector,ctxpp_total,ctxpp_female,ctxpp_male):
        self.ctxpp_id = ctxpp_id
        self.ctxpp_province = ctxpp_province
        self.ctxpp_district = ctxpp_district
        self.ctxpp_sector = ctxpp_sector
        self.ctxpp_total = ctxpp_total
        self.ctxpp_female = ctxpp_female
        self.ctxpp_male = ctxpp_male
    def __str__(self):
        return("  pop_id = {0}\n"
               "  pop_prov = {1}\n"
               "  pop_dist = {2}\n"
               "  pop_sect = {3}\n"
               "  pop_total = {4}\n"
               "  pop_female = {5}\n"
               "  pop_male = {6}\n"
               .format(self.ctxpp_id, self.ctxpp_province,self.ctxpp_district,self.ctxpp_sector,self.ctxpp_total,self.ctxpp_female,self.ctxpp_male))

wb = open_workbook('popul.xls')
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
        q='INSERT INTO cartix_population(ctxpp_id,ctxpp_province,ctxpp_district,ctxpp_sector,ctxpp_total,ctxpp_female,ctxpp_male) VALUES (%s,%s,%s,%s,%s,%s,%s);'
        data=(item.ctxpp_id,item.ctxpp_province,item.ctxpp_district,item.ctxpp_sector,item.ctxpp_total,item.ctxpp_female,item.ctxpp_male)
        cur.execute(q,data)
        #cur.execute('INSERT INTO ctxp(ctxp_id,ctxp_name) VALUES (?,?)',(item.ctxp_id,item.ctxp_name))
        con.commit()

for item in items:
    print item

#    print("Accessing one single value (eg. Prov_name): {0}".format(item.ctxp_name))
#    print
