from flask import Flask, g, redirect, render_template, request, url_for, session, flash
from flask_mysqldb import MySQL
import yaml

app = Flask(__name__)
app.secret_key='supersecretkey'

# configure db connection
db = yaml.load(open('db.yaml'))
app.config['MYSQL_HOST'] = db['mysql_host']
app.config['MYSQL_USER'] = db['mysql_user']
app.config['MYSQL_PASSWORD'] = db['mysql_password']
app.config['MYSQL_DB'] = db['mysql_db']

mysql = MySQL(app)

@app.before_request
def before_request():
    g.user = None


@app.route('/')
def base():
    return render_template('base.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # process login form
        # redirect to /me if authentication successful
        # redirect back to /login if not

        userDetails = request.form
        username = userDetails['username']
        password = userDetails['password']

        cur = mysql.connection.cursor()
        cur.execute('SELECT * FROM users WHERE username = %s AND password = %s', (username, password))

        account = cur.fetchone()

        if account:
            session['logged_in'] = True
            session['username'] = username

            flash('You are now logged in!', 'success')

            return redirect(url_for('me'))

        else:
            flash("Incorrect username/password!", "danger")
        
        pass
    # if user is logged in already, redirect to /me
    if g.user:
        return redirect(url_for('me'))

    return render_template('login.html')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        # process signup form
        # create new user
        # redirect to /login
        userDetails = request.form
        username = userDetails['username']
        password = userDetails['password']
        confirm = userDetails['confirm']

        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO users(username, password, confirm) VALUES(%s, %s, %s)",(username, password, confirm))
        mysql.connection.commit()
        cur.close()

        flash('You are now signed up and can log in!', 'success')

        return redirect(url_for('login'))

        pass
    # if user is logged in already, redirect to /me
    return render_template('signup.html')


@app.route('/me', methods=['GET'])
def me():
    # if the user is not logged in, redirect to /login
    if not g.user:
        return redirect('login')
    return render_template('me.html')


@app.route('/logout', methods=['GET'])
def logout():
    # log user out
    # redirect to /login
    session.clear()
    flash('You are now logged out', 'success')
    return redirect(url_for('login'))
