import psycopg2
import numpy as np 
import matplotlib.pyplot as mp
con = psycopg2.connect("dbname=postgres user=postgres host=192.168.138.51 port=5432 password=VEST777berto")

cur = con.cursor()
cur.execute("SELECT x, y FROM lab_view.fn ORDER BY x;")

arr = cur.fetchall()

cur.close()
con.close()

x, y = np.array(arr).T

mp.plot(x, y)

mp.title('sine wave')
mp.xlabel('x')
mp.ylabel('y = sin(x)')

mp.grid(True, which='both')
mp.axhline(y=0, color='k')

mp.show()
