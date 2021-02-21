from flask import Flask, redirect, url_for, render_template, request, session
from datetime import timedelta


app = Flask(__name__)
# Secret key
app.secret_key = "a3#m6CEBqkXYcsfryn5rFA7"
app.permanent_session_lifetime = timedelta(minutes=5)


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


@app.route('/user')
def user():
    if "user" in session:
        user = session['user']
        return f"<h1>{user}</h1>"
    else:
        return redirect(url_for('login'))


@app.route('/logout')
def logout():
    session.pop('user', None)   # It removes the 'user' key's value.
    return redirect(url_for('login'))

if __name__=='__main__':
    app.run(debug=True)