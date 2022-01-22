from flask import Flask, render_template, url_for
app = Flask(__name__)


@app.route("/")
@app.route("/login")
def login():
  return render_template('login.html')

@app.route("/home")
def home():
  return render_template('home.html')

@app.route("/profile")
def about():
  return render_template('profile.html')

if __name__ == '__main__':
  app.run(debug=True, port=5001) 