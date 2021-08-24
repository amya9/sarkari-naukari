from flask import Flask , render_template
from flask_pymongo import PyMongo


app = Flask(__name__)

# mongo_client = PyMongo(app , uri="mongodb+srv://username:password@cluster0.h1dw4.mongodb.net/category?retryWrites=true&w=majority".format(username , password))
app.config["MONGO_URI"] = "mongodb+srv://amya:amit9799@cluster0.h1dw4.mongodb.net/myAdmin?retryWrites=true&w=majority"
mongodb_client = PyMongo(app)
db = mongodb_client.db


@app.route("/")
def home_page():
    collect = db.get_collection('category')
    category_collection = collect.find()
    print('success')
    return render_template("homepage.html" , category_collection = category_collection)

@app.route("/latest_jobs")
def latest_jobs():
    return render_template("latestJob.html")

@app.route("/answer_keys")
def answer_keys():
    return render_template("answerKey.html")

@app.route("/admit_card")
def admit_card():
    return render_template("admitCard.html")

@app.route("/results")
def results():
    return render_template("result.html")


@app.route("/admissions")
def admissions():
    return render_template("admission.html")

@app.route("/contact_us")
def contact_us():
    return render_template("contactUs.html")


@app.route("/items")
def item():
    return render_template("item.html")

if __name__ == "__main__":
    app.run(debug=True , port=5001)