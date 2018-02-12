#!/usr/bin/python

import MySQLdb

# Open database connection
db = MySQLdb.connect("localhost","root","Rutvij123","RATING" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

movieid = []
userid = []
rating = []


sql = "SELECT * FROM RATING"
try:
   # Execute the SQL command
   cursor.execute(sql)
   # Fetch all the rows in a list of lists.
   results = cursor.fetchall()
   for row in results:
      user_id = int(row[0])
      movie_id = int(row[1])
      rating_r = float(row[2])

      userid.append(user_id)
      movieid.append(movie_id)
      rating.append(rating_r)
except:
   print "Error: unable to fetch data"

# disconnect from server
db.commit()
db.close()
