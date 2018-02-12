#!/usr/bin/python
import csv
import MySQLdb

with open('rating1.csv') as csvfile:
    readCSV1 = csv.reader(csvfile,delimiter=',')

    mov_id = []
    mov_rat = []
    user_id = []

    for row in readCSV1:
        userid = int(row[0])
        movid = int(row[1])
        movrat = float(row[2])

        user_id.append(userid)
        mov_id.append(movid)
        mov_rat.append(movrat)


#print user_id
# Open database connection
db = MySQLdb.connect("localhost","root","Rutvij123","RATING" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

for i in range(len(user_id)):
    sql = "INSERT INTO RATINGS VALUES (%s,%s,%s)"%(user_id[i],mov_id[i],mov_rat[i])
    #sql = "INSERT INTO RATINGS VALUES ("+str(user_id[i])+","+str(mov_id[i])+","+str(mov_rat[i])+");"
    try:
    # Execute the SQL command
        cursor.execute(sql)
    # Fetch all the rows in a list of lists.
    except:
        print "Error: unable to fetch data"

db.commit()
# disconnect from server
db.close()

print "Done"
