from flask import abort, redirect, url_for, Flask
app = Flask(__name__)

@app.route("/")
def index():
    return redirect(url_for('static', filename='index.html'))
	
def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.debug = True
    app.run()
