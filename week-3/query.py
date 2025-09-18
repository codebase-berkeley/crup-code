import sqlite3

# Connect to (or create) the database
conn = sqlite3.connect("students.db")
cursor = conn.cursor()

# TODO: Write SQL to create the table `students` with:
#   - id INTEGER PRIMARY KEY
#   - name TEXT
#   - grade INTEGER

# TODO: Insert at least 3 rows of data (name + grade)

# Commit inserts
conn.commit()

# TODO: Write query to select all students with grade >= 90
cursor.execute("SELECT * FROM students WHERE grade >= 90;")
rows = cursor.fetchall()

print("High scoring students:")
# TODO: loop through rows and print them

conn.close()


