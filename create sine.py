import psycopg2
con = psycopg2.connect("dbname=postgres user=postgres host=192.168.138.51 port=5432 password=VEST777berto")
cur = con.cursor()
cur.execute("SELECT x, y FROM lab05.fn ORDER BY x")

arr = cur.fetchall()

cur.close()
con.close()

f = open("sine.csv", "w")

for row in arr:
    f.write(f"{row[0]},{row[1]}\n")

f.close()

