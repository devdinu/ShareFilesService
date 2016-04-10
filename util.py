from config import Config
import json

class Util:

    @classmethod
    def get_file_obj(cls, record):
        return File(record).__dict__

    @staticmethod
    def get_mongo_consitent(name):
        return name.replace(Config.DOT_CHAR, Config.DOT_UNICODE)

    @staticmethod
    def get_convert_unicodes_to_dot(name):
        return name.replace(Config.DOT_UNICODE, Config.DOT_CHAR)


class File:

    def __init__(self, record):
        self.file_name = Util.get_convert_unicodes_to_dot(record.get('file_id'))
        self.id = str(record.get('_id'))
        self.created_at = record.get('_id').generation_time.strftime("%x")
