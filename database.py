import mysql.connector as my
import os
def database():
    return my.connect(
        host=os.getenv("MYSQLHOST", "switchyard.proxy.rlwy.net"), 
        user=os.getenv("MYSQLUSER", "root"),
        passwd=os.getenv("MYSQLPASSWORD", "xgVCyGuDSUREwbYwJMhWpTvyWrprfXWp"),
        port=int(os.getenv("MYSQLPORT", 3306)),
        database=os.getenv("MYSQLDATABASE", "railway")
    )
db=database()
cr=db.cursor()
cr.execute('create database if not exists railway')
cr.execute('create table if not exists calcs(id int auto_increment primary key,name varchar(25)' \
',CS int,Math1 int ,Discrete int,Elctronics int,Creative_thinking int' \
',Technical_writing int,GPA DECIMAL)')
db.commit()
cr.close()
db.close()
