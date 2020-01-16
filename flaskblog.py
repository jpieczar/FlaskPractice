from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config["SECRET_KEY"] = "9077b574209596b53e2e80d97bd88043"
# A SECRET_KEY protects against forgery attacks.

posts = [
    {
        "author": "Jonathan Pieczara",
        "title": "Blog Post 1",
        "content": "First post content",
        "date_posted":  "7 Jan 2020"
    },
    {
        "author": "Bob Martin",
        "title": "Blog Post 2",
        "content": "Second post content",
        "date_posted":  "8 Jan 2020"
    }
]

@app.route("/")
@app.route("/home")
@app.route("/index")
def home():
    return render_template("home.html", posts=posts)
# -or-
# You can use:
#     return '''
#     <h1>Home Page</h1>
#     <p>This is a WELCOME page.</p>
#     <p>Wow. This is really cool.</p>
#     '''

@app.route("/about")
@app.route("/info")
def about():
    return render_template("about.html", title="Blog")

@app.route("/register", methods=["GET", "POST"])
@app.route("/signup", methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f"Account created for {form.username.data}!", 'success')
        return redirect(url_for('home'))
    return render_template("register.html", title="Register", form=form)

@app.route("/login")
@app.route("/signin")
def login():
    form = LoginForm()
    return render_template("login.html", title="Login", form=form)

if __name__ == '__main__':
    app.run(debug=True)