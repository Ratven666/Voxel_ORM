# from utils.create_database import create_db
from config import FILE_NAME
from classes.db_models import *
from utils.create_database import *
from classes.db_models.ImportedFileDB import *

import time

create_db()

scan = ScanDB("scan")

time0 = time.time()
scan.load_scan_from_file(file_name=FILE_NAME)
print(time.time() - time0)


scan = ScanDB("scan2")

time0 = time.time()
scan.load_scan_from_file(file_name=FILE_NAME)
print(time.time() - time0)

time0 = time.time()
for p in scan:
    pass
print(time.time() - time0)
