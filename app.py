from flask import Flask
from flask_pymongo import PyMongo
import json


app = Flask(__name__)
mongodb_client = PyMongo(app, uri="mongodb+srv://eman:12345@cluster0.jd8un.mongodb.net/bbcnews?retryWrites=true&w=majority")
db = mongodb_client.db


print(mongodb_client.__dict__)


@app.route("/")
def home_page():
    # titles = db.todos.find({"title"})
    # #print(titles[0])
    # return jsonify([todo for todo in titles])
    news = db.bbcnews.find()
    response = []
    for document in news:
        document['_id'] = str(document['_id'])
        response.append(document)
    return json.dumps(response)

app.run()