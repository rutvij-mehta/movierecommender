import csv
import numpy as np



with open('movies.csv') as csvfile:
    readCSV = csv.reader(csvfile,delimiter=',')

    movie_id = []
    movie_name = []
    movie_rating = []
    mp_id = []



    for row in readCSV:
        #row[3] = row[3].replace(u'\xa0', u'')
        #row[4] = float(row[4])
        mpid = int(row[0])
        movid = int(row[1])
        moviename = row[2]

        mp_id.append(mpid)
        movie_id.append(movid)
        movie_name.append(moviename)
        #movie_rating.append(movie_r)

    #print(movie_id)

    #print(len)

with open('ratings.csv') as csvfile:
    readCSV1 = csv.reader(csvfile,delimiter=',')

    user_vs_mov= []
    mov_id = []
    mov_rat = []
    user_id = []
    primid = []

    for row in readCSV1:
        userid = int(row[0])
        movid = int(row[1])
        movrat = float(row[2])

        user_id.append(userid)
        mov_id.append(movid)
        mov_rat.append(movrat)

    for i in range(len(mov_id)):
        x = mov_id[i]
        y = movie_id.index(x)
        primid.append(mp_id[y])


    for i in range(len(mov_id)):
        fd = open('rating1.csv','a')
        myCsvRow = str(user_id[i])+","+str(primid[i])+","+str(mov_rat[i])+"\n"
        fd.write(myCsvRow)
        fd.close()

    print("Done")
