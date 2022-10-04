"""Greeting Flask app."""

from random import choice

from flask import Flask, request

# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible',
    'wonderful', 'smashing', 'lovely']


@app.route('/')
def start_here():
    """Home page."""

    return "<!doctype html><html>Hi! This is the home page.<p><a href='/hello'>Go to hello page</a></p></html>"


@app.route('/hello')
def say_hello():
    """Say hello and prompt for user's name."""

    return """
    <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      <body>
        <h1>Hi There!</h1>
        <form action="/greet">
          What's your name? <input type="text" name="person">
          <label for="compliment">Choose a compliment: </label>
          <select name="compliment">
            <option value='awesome'>awesome</option>
            <option value='terrific'>terrific</option>
            <option value='fantastic'>fantastic</option>
            <option value='neato'>neato</option>
            <option value='fantabulous'>fantabulous</option>
            <option value='wowza'>wowza</option>
            <option value='oh-so-not-meh'>oh-so-not-meh</option>
            <option value='brilliant'>brilliant</option>
            <option value='ducky'>ducky</option>
            <option value='coolio'>coolio</option>
            <option value='incredible'>incredible</option>
            <option value='wonderful'>wonderful</option>
            <option value='smashing'>smashing</option>
            <option value='lovely'>lovely</option>
          </select>
          <input type="submit" value="Submit">
        </form>
        <form action="/diss">
          <p>
            What's your name? <input type="text" name="person">
            <label for="diss">Choose a diss</label>
            <input type="radio" name="diss" value="you stink!"> you stink!
            <input type="radio" name="diss" value="go away!"> go away!
            <input type="radio" name="diss" value="you're the worst!"> you're the worst!
            <input type="radio" name="diss" value="you can't sit with us"> you can't sit with us
            <input type="submit" value="Submit">
          </p>
        </form>
      </body>
    </html>
    """
@app.route('/diss')
def diss_person():
    """Get user by name."""

    player = request.args.get("person")

    diss = request.args.get("diss")

    return f"""
    <!doctype html>
    <html>
      <head>
        <title>A Diss</title>
      </head>
      <body>
        Hi, {player}! I think {diss}!
      </body>
    </html>
    """

@app.route('/greet')
def greet_person():
    """Get user by name."""

    player = request.args.get("person")

    compliment = request.args.get("compliment")

    return f"""
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi, {player}! I think you're {compliment}!
      </body>
    </html>
    """


if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True, host="0.0.0.0")
