from flask import Flask ,render_template
app = Flask(__name__)

@app.route("/name")
def hello():
    hero = "Harshit"
    return render_template('index1.html',hero = hero)
if __name__ == "__main__":
    app.run()
