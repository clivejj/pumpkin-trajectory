from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods = ["POST", "GET"])
def root():
    return render_template("form.html")

@app.route("/login", methods = ["POST", "GET"])
def login():
    return render_template("login.html", username = request.form["username"],
                           method = request.method)

if __name__ == '__main__':
    app.debug = True
    app.run()
