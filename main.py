# from utils.create_database import create_db
from config import FILE_NAME
from db_models import *
from utils.create_database import *
from utils.parsers.TxtParser import TxtParser

import time

create_db()

scan = Scan("scan")
time0 = time.time()

parser = TxtParser(scan)

time1 = time.time()
print(time1 - time0)


scan.load_scan_from_file(file_name=FILE_NAME)
time2 = time.time()
print(time2 - time1)
