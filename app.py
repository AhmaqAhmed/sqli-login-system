from flask import Flask, render_template, request
import pymysql as p

app = Flask(__name__)

def login(usr, pswd):
    try:
        db = p.connect(
            host="localhost",
            user="root",
            password="root",
            database="sqli_lab",
            connect_timeout=3
        )
        c = db.cursor()

        q = f"SELECT * FROM users WHERE username = '{usr}' AND password = '{pswd}'"
        print("executing query:", q)

        c.execute(q)
        res = c.fetchone()

        c.close()
        db.close()
        return bool(res)

    except Exception as e:
        print("DB ERROR:", e)
        return False


@app.route("/", methods=["GET", "POST"])
def index():
    msg = None
    redirect_url = None

    if request.method == "POST":
        usr = request.form.get("username")
        pswd = request.form.get("password")

        if login(usr, pswd):
            msg = ("Login successful", "success")
            redirect_url = "/sec"
        else:
            msg = ("Login failed", "error")

    return render_template("login.html", msg=msg, redirect_url=redirect_url)


@app.route("/sec")
def sec():
    return render_template("sec.html")


if __name__ == "__main__":
    app.run(debug=True)
