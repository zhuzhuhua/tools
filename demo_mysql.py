# !/usr/bin/python
import MySQLdb
import time

conn = MySQLdb.connect(
    host="#118.31.40.169#",
    user="devops",
    passwd="7cDhC92G3wCK6GyGERrGBmAyjMciKXGj",
    charset="utf8"
)
cursor = conn.cursor()
cursor.execute(
    "SELECT sub_system_id FROM report_v2.report_sub_systems where sub_system_type= %s order by id desc limit 1", (str,))

# cursor.fetchone()
# cursor.fetchall()