import logging

class logconfig:
    logging.basicConfig(filename='applog.log', level=logging.DEBUG, format='%(asctime)s : %(levelname)s : %(message)s')