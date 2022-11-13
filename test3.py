import logging
logging.basicConfig(filename="Test3.log",level=logging.DEBUG,format='%(levelname)s %(asctime)s %(name)s %(message)s')
try:
    with open('sudh.txt',"r"):
        logging.info("Succesfully it has read the file")
except Exception as e:
    logging.critical("This a solution for us")
    logging.error(e)
