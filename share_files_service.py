from bottle import post, get, default_app, request, default_app, abort
from bson.objectid import ObjectId
from util import Util
from config import Config
import re
import os
import json

collection = Config.collection

@post('/upload/<file_name>')
def share_file(file_name):
    content = request.body.read().decode('utf-8')
    print("saving file:" + file_name)
    return collection.insert({'file_id': Util.get_mongo_consitent(file_name), 'content': content})

@get('/search/<pattern>')
def search_files(pattern):
    return json.dumps({"files": [
        Util.get_file_obj(record) for record in collection.find({'file_id': re.compile(pattern)})
    ]})

@get('/files/<object_id>')
def download_file(object_id):
    try:
        obj_id = ObjectId(object_id)
    except:
        abort(404, "No Record Found !")
    record = collection.find_one({"_id": obj_id})
    return bytes(record.get('content'), 'utf-8') if record else None


@get('/ping')
def ping():
    print("Successful request....")
    return "Pong!"

application = default_app()

if __name__=="__main__":
    Config.enable_reload = True

application.run(reloader=Config.enable_reload)
