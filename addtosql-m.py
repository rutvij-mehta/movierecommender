#!/usr/bin/python
import csv
import MySQLdb

with open('movies.csv') as csvfile:
    readCSV1 = csv.reader(csvfile,delimiter=',')

    mov_id = []
    mov_name = []
    mov_genre = []

    for row in readCSV1:

        movid = int(row[0])
        movname = row[1]
        movgen = row[2]

        mov_id.append(movid)
        mov_name.append(movname)
        mov_genre.append(movgen)


# Open database connection
db = MySQLdb.connect("localhost","root","Rutvij123","RATING" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

for i in range(len(mov_id)):
    sql = "INSERT INTO MOVIES VALUES (%s,%s,%s)"
    #sql = "INSERT INTO RATINGS VALUES ("+str(user_id[i])+","+str(mov_id[i])+","+str(mov_rat[i])+");"

    # Execute the SQL command
    cursor.execute(sql,(str(mov_id[i]),str(mov_name[i]),str(mov_genre[i])))

        #print "Error: unable to fetch data"


# disconnect from server
db.commit()
db.close()

print "Done"
