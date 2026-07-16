import sqlite3

conn = sqlite3.connect("data/sentinel.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS cloudshield_status (
    id INTEGER PRIMARY KEY, 
    alerts_count INTEGER, 
    timestamp TEXT
)
""")
cursor.execute("""
CREATE TABLE IF NOT EXISTS autopilot_status (
    id INTEGER PRIMARY KEY, 
    datasets_profiled INTEGER, 
    timestamp TEXT
)
""")

cursor.execute("INSERT INTO cloudshield_status (alerts_count, timestamp) VALUES (12, datetime('now'))")
cursor.execute("INSERT INTO autopilot_status (datasets_profiled, timestamp) VALUES (5, datetime('now'))")

conn.commit()
conn.close()
print("Database seeded successfully!")