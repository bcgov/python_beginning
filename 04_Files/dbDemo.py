import cx_Oracle
import os

#  cx_Oracle.makedsn(host, port, sid=None, service_name=None,
#  region=None, sharding_key=None, super_sharding_key=None)

# dsn bcgw... = host, port, service_name
dsn = cx_Oracle.makedsn('bcgw-i.bcgov', '1521', service_name='idwdlvr1.bcgov')
print(dsn)
# retrieve the password from the environment variable PSWD
pswd = os.environ['PSWD']
# make a connection
# kjnether is the user.
conn = cx_Oracle.connect('kjnether', pswd, dsn )

sql = 'select * from user_tables'

cur = conn.cursor()

# execute the query

cur.execute(sql)

# iterate over each colun description
cnt = 1
for desc in cur.description:
    print(f'column number {cnt} is named {desc[0]}')
    cnt += 1

# print actual data
cnt = 0
for row in cur:
    if cnt < 10:
        print(row)
    else:
        break
    cnt += 1


