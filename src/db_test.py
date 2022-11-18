import sqlite3
import db
def test_sqlite3_connection():
    with sqlite3.connect('warehouse.db') as con:
        cursor = con.cursor()
        assert list(cursor.execute('SELECT 1')) == [(1,)]

def test_createTable():
    with sqlite3.connect('warehouse.db') as con:
        cursor = con.cursor()
        cursor.execute('SELECT id from votes')
        rows = cursor.fetchall()
        assert len(rows) != 0

def test_createTable2():
    with sqlite3.connect('warehouse.db') as con:
        cursor = con.cursor()
        cursor.execute('SELECT year from votes2')
        rows = cursor.fetchall()
        assert len(rows) != 0

def test_getResult():
    with sqlite3.connect('warehouse.db') as con:
        cursor = con.cursor()
        cursor.execute("SELECT * FROM votes2 where cvw/(SELECT AVG(cvw) FROM votes2) Not Between 0.8 AND 1.2")
        rows = cursor.fetchall()
        assert list(rows) == [(2022, 0, 1),(2022, 1, 3),(2022, 2, 3),(2022, 5, 1),(2022, 6, 1),(2022, 8, 1)]
