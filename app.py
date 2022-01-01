from flask import Flask , render_template , request, redirect , session
from flask_pymongo import PyMongo
import os
import random

# from dotenv import load_dotenv 


app = Flask(__name__)
app.config['SESSION_TYPE'] = 'memcached'
app.config['SECRET_KEY'] = "amit kumar"
# load_dotenv() # use dotenv to hide sensitive credential as environment variables
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
    collect = db.get_collection('Latest Jobs')
    
    # category_list = session.get("category_list" , None)
    # print("category_list === " , category_list)

    # latest_job_category = category_list[0]
    category_name = "Latest Jobs"
    item_collection = collect.find()
    return render_template("latestJob.html" , 
                            category_name = category_name ,
                            item_collection = item_collection)

@app.route("/answer_keys")
def answer_keys():
    collect = db.get_collection('Answer Key')
    answer_key_collection = collect.find()
    return render_template("answerKey.html" , answer_key_collection  = answer_key_collection)

@app.route("/admit_card")
def admit_card():
    collect = db.get_collection('Admit cards')
    admit_card_collection = collect.find()
    return render_template("admitCard.html" , admit_card_collection = admit_card_collection)

@app.route("/results")
def results():
    collect = db.get_collection('Results')
    result_collection = collect.find()
    return render_template("result.html" , result_collection = result_collection)


@app.route("/admissions")
def admissions():
    collect = db.get_collection('Admissions')
    admission_collection = collect.find()
    return render_template("admission.html" , admission_collection = admission_collection)

@app.route("/contact_us")
def contact_us():
    return render_template("contactUs.html")


@app.route("/items")
def item():
    category_name = request.args.get("category_name" , None)
    session['categor'] = category_name
    print("item category name === " , category_name)

    item_collection = db.get_collection(str(category_name))
    print("item get collection === " , item_collection)

    item_collection_data = item_collection.find()
    print("item_collection_data === " , item_collection_data)

    lower_caregory_name = category_name.lower()
    category_collection = db.get_collection("category")

    return render_template("item.html" ,
                            category_collection = category_collection ,
                            category_name = category_name ,
                            item_collection_data = item_collection_data)


@app.route("/item_detail")
def item_detail():
    category_name = session.get("categor" , None)
    categoryItemArray = []
    item_id = request.args.get("item_id" ,None)
    
    # job id and job category name from nav bar
    job_category_name = request.args.get("category_name" , None)
    job_id_nav = request.args.get("job_id" , None)
    print(f"this is job_id_nav --- {job_id_nav}")
    jobDataNav = db.get_collection(str(job_category_name)).find_one({"_id":job_id_nav})

    print(f"this is job id --- {item_id}")
    print(f"this is job category name --- {category_name}")
    jobData = db.get_collection(str(category_name)).find_one({"_id":item_id})
    
    if jobDataNav:
        jobDataDetails = jobDataNav
    else:
        jobDataDetails = jobData

    print(f"this is job data----{jobData}")

    categoryItemCollection = db.get_collection(str(category_name))
    print(f"this is job categoryItemCollection----{categoryItemCollection}")

    return render_template("itemDetail.html" ,
                        categoryItemCollection = categoryItemCollection ,
                        job_id = item_id , 
                        jobDetail = jobDataDetails)

if __name__ == "__main__":
    app.run(debug=True , port=5003)