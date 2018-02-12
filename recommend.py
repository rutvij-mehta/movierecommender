import numpy as np
from math import sqrt
import MySQLdb

def findmin(sum):
    least = sum[0]      #least element after -1
    leasti = 0
    for i in range(len(sum)):
        if(sum[i]<least and sum[i]!=-1):
            least = sum[i]
            leasti = i

    print least
    return leasti

def findmax(sum):
    maxi = 0
    max1 = sum[0]
    for i in range(len(sum)):
        if(sum[i]>max1 and sum[i]!=0):
            max1 = sum[i]
            maxi = i
    return maxi

def recommend(uid):

    db = MySQLdb.connect("localhost","root","Rutvij123","RATING" )
    cursor = db.cursor()

    movieid = []
    userid = []
    rating = []

    sql = "SELECT * FROM RATINGS ORDER BY uid,mid"
    #INSERT ORDER BY UID IN ABOVE SQL QUERY
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
        print "Error"

    #getUserLength
    sql = 'SELECT COUNT(*) FROM USERS'
    cursor.execute(sql)
    userlength = cursor.fetchone()[0]
    print(userlength)
    #getMovieLength
    sql = 'SELECT COUNT(*) FROM MOVIES'
    cursor.execute(sql)
    movielength = cursor.fetchone()[0]
    print(movielength)
    # disconnect from server
    db.close()

    #--------------------------------------------------------------------
    #GET UVM
    uvm = np.zeros((userlength,movielength))

    k=0
    j=1

    for k in range(len(movieid)):
        if(j==userid[k]):
            uvm[j-1][movieid[k]-1] = rating[k]
        else:
            k -= 1
            j += 1



    """for i in range(672):
        for j in range(9126):
            if uvm[i][j]!=0:
                print uvm[i][j],i,j"""


    #-----------------------------------------------------------------------
    #GET RECOMMENDATION
    lenmovie = movielength
    lenuser = userlength
    sum = np.zeros(lenuser)
    marked1 = np.zeros(lenmovie)
    marked = np.zeros(lenmovie)


    #calculate euclidian distance
    for i in range(lenuser):
        if((uid-1)!=i):
            for j in range(lenmovie):
                sum[i] += (uvm[uid-1][j]-uvm[i][j])*(uvm[uid-1][j]-uvm[i][j])
        elif uid-1==i:
            sum[i] = -1

        if(sum[i]>=0):
            sum[i] = sqrt(sum[i])
            print(sum[i])

    print("Negative",sum[uid-1])
    #find user's closest
    user_closest = findmin(sum)

    print("Recommend",user_closest)

    for j in range(lenmovie):
        if(uvm[user_closest][j] > 0.0):
            print("In first for",j)
            marked1[j] = 1

    for j in range(lenmovie):
        if(uvm[uid-1][j] == 0 and marked1[j]):
            marked[j] = uvm[user_closest][j]
            print(marked[j],j,"In second for")

    #return recommend vector
    for i in range(len(marked)):
        if(marked[i]!=0):
            print(marked[i],i,"In third for")


    print("Max",findmax(marked))
    final1 = np.argsort(marked)[::-1][:10]
    final1 = final1+1

    return final1
