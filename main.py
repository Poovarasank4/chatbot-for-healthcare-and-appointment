from flask import Flask, render_template, request, redirect, url_for, session
from flask.json import jsonify
from flask_mysqldb import MySQL
import MySQLdb.cursors


from werkzeug.utils import redirect

app = Flask(__name__)
app.secret_key = "man"
app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = "bharath@123"
app.config["MYSQL_DB"] = "miniproject"

mysql = MySQL(app)


@app.route("/", methods=["GET", "POST"])
def first():
    if request.method == "POST":
        if request.form.get("doctor") == "DOCTOR":
            return render_template("doctor.html")
        elif request.form.get("user") == "PATIENT/USER":
            return render_template("index.html")
        else:
            pass
    return render_template("firsthomepage.html")


@app.route("/login1", methods=["POST", "GET"])
def login1():
    msg1 = ""
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["EmailID"]
        ps = request.form["password"]
        error = None
        if not name or not name.strip():
            error = "name is missing"
        if not email or not email.strip():
            error = "email is missing"
        if not ps or not ps.strip():
            error = "ps is missing"
        if error:
            msg1 = "please fill out form"
            return render_template("doctor.html", msg1=msg1)
        cursor1 = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor1.execute(
            "SELECT * from appdoc where name=%s AND email=%s AND password=%s",
            (name, email, ps,),
        )
        appdoc = cursor1.fetchone()
        if appdoc:
            session["loggedin"] = True
            session["name"] = appdoc["name"]
            session["email"] = appdoc["email"]
            session["ps"] = appdoc["password"]
            msg = "you have loggedin successfully"
            return redirect("/displayapp")
        else:
            msg1 = "Incorrect password/username"
            return render_template("doctor.html", msg1=msg1)


@app.route("/register1", methods=["POST", "GET"])
def register1():
    if request.method == "POST":
        name = request.form["name"]
        city = request.form["city"]
        address = request.form["address"]
        email = request.form["email"]
        spl = request.form["spl"]
        start = request.form["start"]
        end = request.form["end"]
        password = request.form["password"]
        amount = request.form["amount"]
        error = None
        if not name or not name.strip():
            error = "The name is missing"
        if not city or not city.strip():
            error = "the city us missing"
        if not address or not address.strip():
            error = "The adress is missing"
        if not email or not email.strip():
            error = "email is missing"
        if not spl or not spl.strip():
            error = "The spl is missing"
        if not start or not start.strip():
            error = "start is missing"
        if not end or not end.strip():
            error = "end is missing"
        if not password or not password.strip():
            error = "password is missing"
        if not amount or not amount.strip():
            error = "DOB is missing"
        if error:
            msg1 = "please fill out form"
            return render_template("doctor.html", msg1=msg1)
        cur1 = mysql.connection.cursor()
        cur1.execute(
            "INSERT INTO appdoc(name,city,address,email,spl,start,end,password,amount) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)",
            (name, city, address, email, spl, start, end, password, amount),
        )
        mysql.connection.commit()
        cur1.close()
        session["loggedin"] = True
        session["name"] = name
        session["email"] = email
        session["ps"] = password
        
        return render_template("displayapp.html")


@app.route("/login", methods=["POST", "GET"])
def login():
    msg = ""
    if request.method == "POST":
        username = request.form["name"]
        email = request.form["EmailID"]
        ps = request.form["password"]
        error = None
        if not username or not username.strip():
            error = "name is missing"
        if not email or not email.strip():
            error = "email is missing"
        if not ps or not ps.strip():
            error = "ps is missing"
        if error:
            msg = "please fill out form"
            return render_template("index.html", msg=msg)
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute(
            "SELECT * from users where name=%s AND email=%s AND password=%s",
            (username, email, ps,),
        )
        user = cursor.fetchone()
        if user:
            session["loggedin"] = True
            session["name"] = user["name"]
            session["email"] = user["email"]
            session["ps"] = user["password"]
            msg = "you have loggedin successfully"
            return render_template("home.html", msg=msg)
        else:
            msg = "Incorrect password/username"
            return render_template("index.html", msg=msg)


@app.route("/register", methods=["POST", "GET"])
def register():
    if request.method == "POST":
        name = request.form["Name"]
        email = request.form["EmailID"]
        password = request.form["Password"]
        DOB = request.form["DOB"]
        gender = request.form["gender"]
        phonenumber = request.form["phonenumber"]
        error = None
        if not name or not name.strip():
            error = "The name is missing"
        if not email or not email.strip():
            error = "email is missing"
        if not password or not password.strip():
            error = "password is missing"
        if not DOB or not DOB.strip():
            error = "DOB is missing"
        if not gender or not gender.strip():
            error = "gender is missing"
        if not phonenumber or not phonenumber.strip():
            error = "phonenumber is missing"
        if error:
            msg = "please fill out form"
            return render_template("index.html", msg=msg)
        cur = mysql.connection.cursor()
        cur.execute(
            "INSERT INTO users(name,email,password,DOB,gender,phonenumber) VALUES(%s, %s, %s, %s, %s, %s)",
            (name, email, password, DOB, gender, phonenumber),
        )
        mysql.connection.commit()
        cur.close()
        session["loggedin"] = True
        session["name"] = name
        session["email"] = email
        session["ps"] = password
        return render_template("home.html")


@app.route("/app1", methods=["POST", "GET"])
def app1():
    msg = ""
    if request.method == "POST":
        appname = request.form["nameap"]
        appcity = request.form["cityap"]
        appadd = request.form["appadd"]
        appdate = request.form["date"]
        apps = request.form["speciallist"]
        appst = request.form["start"]
        append = request.form["end"]
        appday = request.form["day"]
        appamt = request.form["amt"]
        error = None
        if not appname or not appname.strip():
            error = "missing"
        if not appcity or not appcity.strip():
            error = "missing"
        if not appadd or not appadd.strip():
            error = "missing"
        if not appdate or not appdate.strip():
            error = "name is missing"
        if not apps or not apps.strip():
            error = "missing"
        if not appst or not appst.strip():
            error = "email is missing"
        if not append or not append.strip():
            error = "ps is missing"
        if not appday or not appday.strip():
            error = "appday is missing"
        if error:
            msg1 = "please fill out form"
            return render_template("doctor1.html", msg1=msg1)
        cur1 = mysql.connection.cursor()
        cur1.execute(
            "INSERT INTO app(appname,appcity,appadd,appdate,apps,appst,append,appday,appamt) VALUES(%s,%s,%s,%s, %s, %s, %s, %s ,%s)",
            (appname, appcity, appadd, appdate, apps, appst, append, appday, appamt),
        )
        mysql.connection.commit()
        cur1.close()
        return render_template("doctor2.html")


@app.route("/search", methods=["POST"])
def search():
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute(
        "SELECT * from appdoc where city=%s AND spl=%s",
        (request.form.get("city"), request.form.get("spl"),),
    )
    appdoc = cursor.fetchall()
    print(appdoc)
    data = {}
    data["city"] = request.form.get("city")
    data["spl"] =  request.form.get("spl")
    return render_template("appointment.html", appdoc=appdoc,data=data)


@app.route("/complete", methods=["POST"])
def complete():
    r = request.form
    # print(r)
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute(
        "insert into aps (username,doctname,msg,date,finish) VALUES(%s, %s, %s, %s ,%s)",
        (session["name"], r["appdoc"], r["msg"], r["date"], False),
    )
    mysql.connection.commit()
    cursor.close()
    return render_template(
        "profile.html", appdoc=r["appdoc"], msg=r["msg"], date=r["date"]
    )



@app.route("/home")
def home():
    return render_template("home.html")


@app.route("/myprofile")
def myprofile():
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute("SELECT * from users where name=%s ", (session["name"],))
    user = cursor.fetchone()
    print(user, flush=True)
    return render_template("myprofile.html", user=user)


@app.route("/myprofiledoc")
def myprofiledoc():
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute("SELECT * from appdoc where name=%s ", (session["name"],))
    user = cursor.fetchone()
    print(user, flush=True)
    return render_template("myprofiledoc.html", user=user)


@app.route("/displayapp")
def displayapp():
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute(
        "SELECT username,msg,date from aps where doctname=%s ", (session["name"],)
    )
    appointment = cursor.fetchall()
    print(appointment)
    return render_template("displayapp.html", appointment=appointment)



@app.route("/appointment")
def appointment():
    return render_template("appointment.html")


@app.route("/history")
def history():
    return render_template("history.html")


@app.route("/contactdoctor")
def contactdoctor():
    return render_template("contactdoctor.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True)