from flask import Flask, redirect, url_for, render_template, request, session, flash
from datetime import timedelta

app = Flask(__name__)
# Secret key
app.secret_key = "a3#m6CEBqkXYcsfryn5rFA7"

app.permanent_session_lifetime = timedelta(minutes=5)

db = SQLAlchemy(app)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Something if we have post method
        session.permanent = True    # It's going to last as long as defined above.
        user = request.form["nm"]
        session["user"] = user  # Set's data for the session.
        return redirect(url_for("user"))
    else:   # If it was a 'GET' method, we just render the template
        if 'user' in session:
            return redirect('user')
        return render_template('login.html')


@app.route('/user', methods=['POST', 'GET'])
def user():
    email = None
    if "user" in session:
        user = session['user']
        if request.method == 'POST':
            email = request.form['email']
            session['email'] = email
            flash('Email was saved!') 
        else:
            if "email" in session:
                email = session['email']
        return render_template('user.html', email=email)
    else:
        return redirect(url_for('login'))


@app.route('/logout')
def logout():
    if "user" in session:
        flash(f'You have logged out successfully, {session["user"]}.', 'info')
        session.pop('user', None)   # It removes the 'email' key's value.
        session.pop('email', None)
    return redirect(url_for('login'))

if __name__=='__main__':
    app.run(debug=True)