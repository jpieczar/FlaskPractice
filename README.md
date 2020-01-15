# FlaskPractice
This is flask practice. Here I follow the tutorial that Corey Schafer (Youtube) made.

### Notes on how to run flask stuff.

    To simply run your stuff:
    $> export FLASK_APP=filename.py
    $> flask run
    -or-
    $> export FLASK_DEBUG=1
    $> flask run
    -or-
    $> python3 filename.py
    (Only if:
        if __name == "__main__":
            app.run(debug.True)
    exists at the bottom of the file.)

    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    # Below deals with setting up an environment.
    $> pip install flask (Try pip3.)
    $> mkdir myProject
    $> cd myProject
    $> python3 -m venv venv (Creates a virtual environment.)
        (You can name the 2nd 'venv' something else.)
        (This creates a dir where the environment files are stored.)

    (You might have to download and install 'virtualenv'.)

    $> virtualenv venv (Creates a virtual environment.)
    $> source venv/bin/activate (Activate the environment.)
    (venv) $>

    (venv) $> pip install flask (Installs flask.)
    (venv) $> python3
    >>>> import flask
    >>>>
    "Ctrl + d" (As there are no errors, it means that flask is installed
    and we can exit.)

### Forms

    # In order to get forms you first have to install Flask-wtf.
    $> pip3 install flask-wtf

### SECRET_KEY

    # Prevents forgery attacks.
    $> python3
    Python 3.7.6 (default, Jan  6 2020, 08:51:01)
    [Clang 11.0.0 (clang-1100.0.33.12)] on darwin
    Type "help", "copyright", "credits" or "license" for more information.
    >>> import secrets
    >>> secrets.token_hex(16)
    '9077b574209596b53e2e80d97bd88043'
