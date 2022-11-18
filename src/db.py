import json
import sqlite3

f = open("test-resources/samples-votes.jsonl")
conn = sqlite3.connect("warehouse.db")
cur = conn.cursor()


def createTable():
    cur.execute("create table if not exists votes(id integer, postId integer, votetypeid integer, creationDate text)")
    column = ['Id', 'PostId', 'VoteTypeId', 'CreationDate']
    cur.execute("DELETE FROM votes")
    for i in f:
        d = json.loads(i)
        keys = tuple(d[c] for c in column)
        cur.execute("insert into votes values(?,?,?,?)", keys)


def createTable2():
    cur.execute("CREATE TABLE IF NOT EXISTS votes2 (Year INTEGER, Week INTEGER UNIQUE, cvw INTEGER)")
    cur.execute("REPLACE INTO votes2 select year,Week_Number, count(Week_Number) from"
                " (select creationDate, substring(creationDate,0,5) year, strftime(\'%W\', CreationDate) "
                "Week_Number, postId as cnt from votes) group by Week_Number")


def getResult():
    cur.execute("SELECT * FROM votes2 where cvw/(SELECT AVG(cvw) FROM votes2) Not Between 0.8 AND 1.2")
    rows = cur.fetchall()
    for row in rows:
        print("{0}, {1}, {2}".format(str(row[0]), str(row[1]), str(row[2])))


createTable()
createTable2()
getResult()
conn.commit()
cur.close()
