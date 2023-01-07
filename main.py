# from utils.create_database import create_db
from config import FILE_NAME
from db_models import *
from utils.create_database import *
from utils.parsers.TxtParser import TxtParser

import time

create_db()

scan = Scan("scan")
time0 = time.time()

scan.load_scan_from_file(file_name=FILE_NAME)

# for _ in range(10_000):
#     scan.load_scan_from_file(file_name=FILE_NAME)

time1 = time.time()
print(time1 - time0)
