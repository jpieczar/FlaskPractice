from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")
# -or-
# You can use:
#     return '''
#     <h1>Home Page</h1>
#     <p>This is a WELCOME page.</p>
#     <p>Wow. This is really cool.</p>
#     '''

@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == '__main__':
    app.run(debug=True)