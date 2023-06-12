###
# Course: CIS 117 Python programming
# Name: Andres Cheung
# Topics: Creating and Using a Database
# Description: In this lab task you will create a simple working example of a
#              relational database using sqlite3.  Operating from the Python3
#              command line prompt you will execute sqlite statements against
#              the database created.
# Date: 04/25/2023

import sqlite3

# connect to the database (create if not exists)
conn = sqlite3.connect('cheung.db')

# create a cursor object to execute SQL statements
c = conn.cursor()

# create the PopByRegion table if it doesn't already exist
c.execute('''CREATE TABLE IF NOT EXISTS PopByRegion
             (Region TEXT, Population INTEGER)''')

# insert the data into the PopByRegion table
c.execute("INSERT INTO PopByRegion VALUES ('Central Africa', 330993)")
c.execute("INSERT INTO PopByRegion VALUES ('Southeastern Africa', 743112)")
c.execute("INSERT INTO PopByRegion VALUES ('Japan', 100562)")

# commit the changes to the database
conn.commit()

# close the cursor and database connection
c.close()
conn.close()

# import sqlite3
# >>> con = sqlite3.connect('cheung.db')
# >>> cur = con.cursor()
# >>> cur.execute('SELECT Region, Population FROM PopByRegion')
# <sqlite3.Cursor object at 0x102799c70>
# >>> cur.fetchall()
# [('Central Africa', 330993), ('Southeastern Africa', 743112), ('Japan', 100562)]
# >>> cur.execute('SELECT Region, Population FROM PopByRegion ORDER by Region')
# <sqlite3.Cursor object at 0x102799c70>
# >>> cur.fetchall()
# [('Central Africa', 330993), ('Japan', 100562), ('Southeastern Africa', 743112)]
# >>> cur.execute('SELECT Region FROM PopByRegion')
# <sqlite3.Cursor object at 0x102799c70>
# >>> cur.fetchall()
# [('Central Africa',), ('Southeastern Africa',), ('Japan',)]
# >>> cur.execute ('SELECT Region FROM PopbyRegion WHERE Population > 400000')
# <sqlite3.Cursor object at 0x102799c70>
# >>> cur.fetchall()
# [('Southeastern Africa',)]
# >>> cur.execute('SELECT * FROM PopByRegion WHERE Region = "Japan"')
# <sqlite3.Cursor object at 0x102799c70>
# >>> cur.fetchone()
# ('Japan', 100562)
# >>> cur.execute('''UPDATE PopByRegion SET Population = 100600 WHERE Region = "Japan"''')
# <sqlite3.Cursor object at 0x102799c70>
# >>> cur.execute('SELECT * FROM PopByRegion WHERE Region = "Japan"')
# <sqlite3.Cursor object at 0x102799c70>
# >>>
# >>> cur.execute('SELECT * FROM PopByRegion WHERE Region = "Japan"')
# <sqlite3.Cursor object at 0x102799c70>
# >>> cur.fetchone()
# ('Japan', 100600)
# >>> cur.execute('DELETE FROM PopByRegion WHERE Region < "S"')
# <sqlite3.Cursor object at 0x102799c70>
# >>> cur.execute('SELECT * FROM PopByRegion')
# <sqlite3.Cursor object at 0x102799c70>
# >>> cur.fetchall()
# [('Southeastern Africa', 743112)]
# >>> cur.close()
# >>> con.close()
# >>>