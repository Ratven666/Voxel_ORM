# from utils.create_database import create_db
# import db_models
from utils.create_database import *
from utils.parsers.TxtParser import TxtParser

create_db()

parser = TxtParser()

parser.load_data()

