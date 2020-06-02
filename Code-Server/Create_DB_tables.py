
import sqlite3

DB_Name =  "DoAn.db"


Table="""
drop table if exists Temperature_Data ;
create table Temperature_Data (
  id integer primary key autoincrement,
  SensorID text,
  Date_n_Time text,
  Temperature text
);


drop table if exists Humidity_Data ;
create table Humidity_Data (
  id integer primary key autoincrement,
  SensorID text,
  Date_n_Time text,
  Humidity text
);
"""

conn = sqlite3.connect(DB_Name)
curs = conn.cursor()

sqlite3.complete_statement(Table)
curs.executescript(Table)

curs.close()
conn.close()
