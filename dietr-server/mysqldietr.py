import os
import mysql.connector

data = os.getenv("VCAP_SERVICES", [])[0]

cred = data["credentials"]
host = cred["host"].encode("utf8")
user = cred["user"].encode("utf8")
password = cred["password"].encode("utf8")
db = cred["name"].encode("utf8")

con = mysql.connector.connect(host = host, user = user, password = password, database = db)

cur = con.cursor()

# cur.execute("CREATE TABLE IF NOT EXISTS accounts ( id INT UNSIGNED NOT NULL AUTO_INCREMENT, " +
#             "email VARCHAR(254) NOT NULL, passhash CHAR(128) NOT NULL, salt CHAR(128) NOT NULL, PRIMARY KEY (id) )")
# cur.execute("CREATE TABLE IF NOT EXISTS sessions ( session BIGINT NOT NULL, id INT UNSIGNED NOT NULL, " +
#             "PRIMARY KEY (session) )")
# cur.execute("CREATE TABLE IF NOT EXISTS health ( id INT UNSIGNED NOT NULL, PRIMARY KEY (id) )")