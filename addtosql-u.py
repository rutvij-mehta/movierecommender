#!/usr/bin/python
import csv
import MySQLdb

with open('user.csv') as csvfile:
    readCSV1 = csv.reader(csvfile,delimiter=',')

    user_id = []
    user_email = []


    for row in readCSV1:

        userid = int(row[0])
        useremail = row[2]

        user_id.append(userid)
        user_email.append(useremail)

print user_id
# Open database connection
db = MySQLdb.connect("localhost","root","Rutvij123","RATING" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

for i in range(len(user_id)):
    sql = "INSERT INTO USERS VALUES (%d,'',%s,'')"%(user_id[i],str(user_email[i]))
    #sql = "INSERT INTO RATINGS VALUES ("+str(user_id[i])+","+str(mov_id[i])+","+str(mov_rat[i])+");"

    # Execute the SQL command
    cursor.execute(sql)

        #print "Error: unable to fetch data"


# disconnect from server
db.commit()
db.close()

print "Done"
