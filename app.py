
# from flask import Flask, render_template

# app = Flask(__name__)

# @app.route('/')
# def HELLO_WORLD():
#     return render_template('index.html')

# if __name__ == "__main__":
#     app.run(debug=True)

from flask import Flask, render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST'] = "localhost"
app.config['MYSQL_USER'] = "root"
app.config['MYSQL_PASSWORD'] = "Rajan@1234"
app.config['MYSQL_DB'] = "game1"

mysql = MySQL(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        Name = request.form['Name']
        Subject = request.form['Subject']
        Email = request.form['Email']
        Your_Message = request.form['Your_Message']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO player1 (Name,Subject, Email,Your_Message) VALUES (%s, %s,%s,%s)", (Name,Subject, Email,Your_Message))
        mysql.connection.commit()
        cur.close()
        return "success"
    else:
        return render_template('index3.html')

if __name__ == "__main__":
    app.run(debug=True)
