from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from Google App Engine Demo Application!"

@app.route("/about")
def about():
    return "This is a simple web application created to understand Google App Engine."

if __name__ == "__main__":
    app.run(host="localhost", port=8080, debug=True)

#gcloud init
#gcloud app create
#gcloud app deploy
#gcloud app browse