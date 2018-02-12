import csv
import numpy as np



with open('movies.csv') as csvfile:
    readCSV = csv.reader(csvfile,delimiter=',')

    movie_id = []
    movie_name = []
    movie_rating = []



    for row in readCSV:
        #row[3] = row[3].replace(u'\xa0', u'')
        #row[4] = float(row[4])
        movieid = int(row[0])
        moviename = row[1]

        movie_id.append(movieid)
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
    count = [0]*671  #Number of movies rated by every user. Hardcoded 671

    for row in readCSV1:
        userid = int(row[0])
        movid = int(row[1])
        movrat = float(row[2])

        user_id.append(userid)
        mov_id.append(movid)
        mov_rat.append(movrat)

    test = []   #Test Matrix
    final = []  #User vs Movies vs Rating Matrix
    length = len(user_id)
    k=0
    j=1
    for i in range(length):
        if(j == user_id[k]):
            count[j-1] += 1
            test.append([mov_id[k],mov_rat[k]])
            k += 1
        else:
            final.append(test)
            test = []
            j += 1

    print(final[0][1])
    u= int(input("Enter user id and movie id\n"))
    m=input()
    print(final[u].index(m))
    #print(final[u-1][final[u].index(m)][1])
    #print(final[user_id.index(u)][mov_id.index(m)][])
    #print(count)
