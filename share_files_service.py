from bottle import post, get, default_app, request
from config import Config

import os
import json
import pdb

collection = Config.collection

def get_mongo_consitent(name):
    return name.replace(Config.DOT_CHAR, Config.DOT_UNICODE)


@post('/upload/<file_name>')
def share_file(file_name):
    content = request.body.read().decode('utf-8')
    print("saving file:" + file_name)
    return collection.insert({'file_id': get_mongo_consitent(file_name), 'content': content})

@get('/ping')
def ping():
    print("Successful request....")
    return "Pong!"

application = default_app()

if __name__=="__main__":
    application.run(debug=True)
