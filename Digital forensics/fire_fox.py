import sqlite3
import os

# Path to the places.sqlite file
profile_path = os.path.expanduser("/home/kali/.mozilla/firefox/hf9j07ga.default-esr/places.sqlite")

# Connect to the SQLite database
conn = sqlite3.connect(profile_path)
cursor = conn.cursor()

# Query to get history
query = "SELECT url, title, visit_count, last_visit_date FROM moz_places ORDER BY last_visit_date DESC;"
cursor.execute(query)

# Fetch and print results
for row in cursor.fetchall():
    print(f"URL: {row[0]}\nTitle: {row[1]}\nVisit Count: {row[2]}\nLast Visit Date: {row[3]}\n")

# Close the connection
conn.close()
