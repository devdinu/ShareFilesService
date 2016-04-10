from pymongo import MongoClient
import os

class Config():
    uri = os.environ.get('OPENSHIFT_MONGODB_DB_URL', "mongodb://localhost:27017/sharefiles")
    collection = MongoClient(uri).sharefiles.files
    DOT_CHAR = "."
    DOT_UNICODE = "\\uff0"
    enode_format = 'utf-8'
    enable_reload = False
