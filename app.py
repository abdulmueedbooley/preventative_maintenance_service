import psycopg2

conn = psycopg2.connect(host = "localhost", dbname = "postgres", user = "postgres", password = "@bdulmu33d", port = 5050)

cur = conn.cursor()

cur.execute(""" INSERT INTO supplier(supplier_id, supplier_name, supplier_contact, supplier_email,
supplier_phone, supplier_address) VALUES(1, 'abdul', 'boolex', 'testing.email', '0662232699', '67 burger street') """)

conn.commit()

cur.close()