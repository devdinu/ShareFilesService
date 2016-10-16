from bottle import post, get, default_app, request, default_app, abort, HTTPResponse, delete
from bson.objectid import ObjectId
from util import Util
from config import Config
import re
import os
import json
import uuid

collection = Config.collection
application = default_app()

@post('/users/<user_id>/files/<file_name>')
def share_file(file_name, user_id):
    content = request.body.read().decode('utf-8')
    print("saving file:" + file_name)
    collection.insert({'file_id': Util.get_mongo_consitent(file_name), 'content': content, 'user_id': user_id})
    return HTTPResponse(status=201, body=str(user_id))

@get('/users/<user_id>/files/search')
def search_files(user_id):
    pattern = request.params.get('pattern')
    return json.dumps({"files": [
        Util.get_file_obj(record) for record in collection.find(
            {'user_id': user_id, 'file_id': re.compile(pattern)})
    ]})

@get('/files/<object_id>')
def download_file(object_id):
    try:
        obj_id = ObjectId(object_id)
    except:
        abort(404, "No Record Found !")
    record = collection.find_one({"_id": obj_id})
    return bytes(record.get('content'), 'utf-8') if record else None

@get('/users/create')
def create_user():
    return str(uuid.uuid4())

@get('/ping')
def ping():
    print("Successful request....")
    return "Pong!"

@delete('/users/<user_id>/files/<file_object_id>')
def delete_file(user_id, file_object_id):
    try:
        oid = ObjectId(file_object_id)
    except:
        abort(404, "No Record Found !")
    if oid: return collection.remove({'_id': oid, 'user_id': user_id})


if __name__=="__main__":
    application.run(reloader=Config.enable_reload)


