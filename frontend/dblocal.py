#db.py
import os
import static
from flask import jsonify
import pymysql

db_user = "root"
db_password = "nehagoel8"
db_name = "MKGames"
db_connection_name = "localhost"

def open_connection():
    conn = ""
    try:
        conn = pymysql.connect(user=db_user, password=db_password,host=db_connection_name, database=db_name,charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
        if (conn):
            print("Open Connection with mysql server")
        else:
            print("Closed Connection with mysql server")

    except pymysql.MySQLError as e:
        print(e)
    return conn


def insertData(sql):
    conn = open_connection()
    try:
        with conn.cursor() as cursor:
      # Read a single record
            cursor.execute(sql)
            conn.commit()
    finally:
        conn.close()
        return "Saved successfully."
"""
if __name__ == '__main__':
    sql = 'INSERT INTO Users (firstname,lastname,password) VALUES ("rajeev","goel","rg")'
    print(sql)
    insertData(sql)
    insertData("select * from Users")
"""