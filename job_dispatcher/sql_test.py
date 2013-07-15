import psycopg2 as pg

conn = pg.connect("dbname=django user=lucas password=password")
cur = conn.cursor()

try:
	cur.execute("DROP TABLE IF EXISTS test")
	cur.execute("CREATE TABLE test ();")
	print "table created"
	
	conn.commit()
except Exception as e:
	print e
	raise ValueError("fuu=")

print "Should now break"

try:
	conn = pg.connect("dbname=asdf user=lucas")
	cur = conn.cursor()

except Exception as e:
	print e
	raise ValueError("You must specify the correct database! Error: %s" % e)
