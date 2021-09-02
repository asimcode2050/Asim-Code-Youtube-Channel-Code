''' Channel : Asim Code 
Browser History using Python
https://youtu.be/yWU8ynQ_tKs
'''
import os
import sqlite3
con  = sqlite3.connect('/home/asimcode/.config/google-chrome/Default/History')
cur = con.cursor()
cur.execute("select url, title, visit_count, last_visit_time from urls")
results = cur.fetchall()
for result in results:
    print(result)
