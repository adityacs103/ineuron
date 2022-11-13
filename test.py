# import logging
# logging.basicConfig(filename="Test2.log", level=logging.DEBUG,
#                     format='%(asctime)s %(name)s %(levelname)s %(message)s')
# logging.info("THis is my time stamp")
import logging
logging.basicConfig(filename="Test2.log",level=logging.INFO, format='%(levelname)s %(name)s %(asctime)s %(message)s')
def devide(a,b):
    logging.info("the number entred by the user is %s and %s",a,b)
    try:
        logging.info("we are in function")
        dev=a/b
        logging.info("we have completed division operation")
        return dev
    except Exception as e:
        logging.exception(e)

result=devide(3,0)
logging.info("Result=%s",result)


