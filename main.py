import os
import time
from sys import argv

from src.script import convert_to_db

if __name__ == '__main__':
    path = os.path.abspath(argv[1])
    start_time = time.time()
    convert_to_db(import_file=argv[1], table_name=argv[2])
    print("--- %s seconds ---" % (time.time() - start_time))