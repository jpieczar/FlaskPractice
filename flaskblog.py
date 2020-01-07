from flask import Flask, render_template, url_for
app = Flask(__name__)

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
def about():
    return render_template("about.html", title="Blog")

if __name__ == '__main__':
    app.run(debug=True)