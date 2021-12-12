#!/usr/bin/env python

import logging
import random
import time
import datetime

while True:

    number = random.randrange(0,5)
    logging.getLogger().setLevel(logging.INFO)
    logging.basicComfig(filename='/var/log/app/logger.txt', format='{"timestamp":"%(asctime)s", "level":"%(levelname)s", "message":"%(message)s"}')

    if number == 1:
        logging.info('I am INFO log, hi')

    elif number == 2:
        logging.warning('This is WARNING to you')

    elif number == 3:
        logging.error('ERROR occured')
    elif number == 4:
        logging.critical('UPY4KA следит за тобой!!!1')
    time.sleep(1)
