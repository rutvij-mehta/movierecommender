from __future__ import print_function
from flask import Flask, jsonify, request, json
from recommend import recommend


import MySQLdb

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello"

@app.route("/validate", methods=['GET','POST'])
def validate():
    print("Connected")
    data2= request.get_json(force=True)
    print("Hi")
    print(data2)      #COMMENTED FOR TESTING
    #data2 will consist of {"email":__}
    email = data2["email"]
    print(email)
    password = data2["password"]
    #data1 = request.json
    #email = "rutij@gmail.com"
    #password = "Rutvij"
    db = MySQLdb.connect("localhost","root","Rutvij123","RATING")
    cursor = db.cursor()

    sql = "SELECT * FROM USERS WHERE email='{0}' and password='{1}'".format(email,password)
    try:
        cursor.execute(sql)
    except:
            print("Error")

    js = cursor.fetchone()
    if(js):
        count = 1
    else:
        count = 0

    #c = {"count" : int(count)}
    return jsonify({"count" : count})

@app.route("/register", methods=['GET','POST'])
def register():
    print("in register")
    data = request.get_json(force=True)
    email = data["email"]
    password = data["password"]
    name = data["name"]
    db = MySQLdb.connect("localhost","root","Rutvij123","RATING")
    cursor = db.cursor()

    sql = "SELECT COUNT(*) FROM USERS"
    cursor.execute(sql)

    count = cursor.fetchone()[0]

    print(count)


    sql = "INSERT INTO USERS VALUES({0},'{1}','{2}','{3}')".format(count+1,str(name),str(email),str(password))

    print(sql)

    cursor.execute(sql)

    db.commit()
    return jsonify({"count" : 1})


@app.route("/getdata", methods=['GET','POST'])
def getData():
    data2= request.get_json(force=True)
    email = data2["email"]
    print("Recieved",email)

    db = MySQLdb.connect("localhost","root","Rutvij123","RATING")
    cursor = db.cursor()

    movieid = []
    moviename = []
    moviegenre = []

    sql = "SELECT * FROM MOVIES"
    try:

        cursor.execute(sql)
        results = cursor.fetchall()
        for row in results:
            movie_id = int(row[0])
            movie_name = row[1]
            movie_genre = row[2]
            movieid.append(movie_id)
            moviename.append(movie_name)
            moviegenre.append(movie_genre)
    except:
        print("Error to fetch data")

    # disconnect from server
    db.close()
    js = []
    print(moviegenre)

    for a,b,c in zip(movieid,moviename,moviegenre):
        js1 = { "mid" : a, "mname" : b, "mgenre" : c}
        js.append(js1)


    f = {"list" : js}
    return jsonify(f)


#WORKING FINE. TESTED
@app.route("/savedata", methods=['POST'])
def save():
    print("in save")
    data = request.get_json(force=True)   #COMMENTED FOR TESTING
    #data1 will consist of {"email":__,"mid" : __,  "rating": __}

    email = data["email"]
    print(data["mid"])
    mid = int(data["mid"])
    print(data["rating"])
    rating = float(data["rating"])
    print(data["rating"])

    db = MySQLdb.connect("localhost","root","Rutvij123","RATING")
    cursor = db.cursor()

    sql = "SELECT uid from USERS WHERE email='{0}'".format(email)
    print(sql)
    cursor.execute(sql)

    uid = int(cursor.fetchone()[0])
    print(uid)

    sql = "INSERT INTO RATINGS VALUES ({0},{1},{2})".format(uid,mid,rating)
    cursor.execute(sql)
    db.commit()

    # disconnect from server
    db.close()
    print("Done savedata")
    return jsonify({"count" : 1})

#WORKING FINE. TESTED
@app.route("/recd", methods = ['GET', 'POST'])
def recd():
    data2= request.get_json(force=True)      #COMMENTED FOR TESTING
    #data2 will consist of {"email":__}
    email = data2["email"]
    print("Recieved",email)

    db = MySQLdb.connect("localhost","root","Rutvij123","RATING")
    cursor = db.cursor()

    sql = "SELECT uid from USERS WHERE email='{0}'".format(email)
    cursor.execute(sql)
    uid = int(cursor.fetchone()[0])
    print("In recd",uid)

    print("UID in recd",uid)
    r = recommend(uid)
    mname = []
    mgenre = []
    mid = r.tolist()

    for i in range(len(mid)):
        sql = "SELECT name,genre FROM MOVIES WHERE mid='{0}'".format(r[i])
        cursor.execute(sql)
        m = cursor.fetchone()
        m_name = m[0]
        m_genre = m[1]

        mname.append(m_name)
        mgenre.append(m_genre)

    js = []
    for a,b,c in zip(mid,mname,mgenre):
        js1 = { "mid" : a, "mname" : b, "mgenre" : c}
        js.append(js1)

    f = {"list" : js}
    return jsonify(f)

@app.route("/test", methods=['GET', 'POST'])
def tes():
    json_data = request.get_json(force=True)
    print(json_data["email"])
    return "Hi"

@app.route("/getgenre", methods=['GET', 'POST'])
def adventure():
    data = request.get_json(force=True)      #COMMENTED FOR TESTING
    print("hi")
    g = data["genre"]
    print(g)
    db = MySQLdb.connect("localhost","root","Rutvij123","RATING")
    cursor = db.cursor()
    genre = []
    mname = []
    mid = []

    sql = "SELECT * FROM MOVIES WHERE genre LIKE '%{0}%'".format(g)

    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        for row in results:
            movie_id = int(row[0])
            movie_name = row[1]
            movie_genre = row[2]
            mid.append(movie_id)
            mname.append(movie_name)
            genre.append(movie_genre)
    except:
        print("Error to fetch data")

    # disconnect from server
    db.close()
    js = []

    mid = mid[0:100]
    mname = mname[0:100]
    genre = genre[0:100]


    for a,b,c in zip(mid,mname,genre):
        js1 = { "mid" : a, "mname" : b, "genre" : c}
        js.append(js1)

    hi = { "list" : js}
    return jsonify(hi)

@app.route("/getcount", methods=['GET','POST'])
def count():
    data2= request.get_json(force=True)
    email = data2["email"]

    db = MySQLdb.connect("localhost","root","Rutvij123","RATING")
    cursor = db.cursor()

    sql = "SELECT uid from USERS WHERE email='{0}'".format(email)
    cursor.execute(sql)
    uid = cursor.fetchone()[0]

    sql = "SELECT COUNT(*) from RATINGS WHERE uid='{0}'".format(uid)
    cursor.execute(sql)
    count = int(cursor.fetchone()[0])

    return jsonify({"count" : count})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
