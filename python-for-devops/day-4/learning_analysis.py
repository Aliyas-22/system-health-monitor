# from logging import *
# basicConfig(filename = 'analysis.log', 
#             level = INFO, 
#             filemode = 'w',
#             )
# try:
#     info("module 2 got completed and module 3 started")
#     warning("the warning message is displaying")
# except Exception as e:
#     warning("Some issue occurred")

import logging
logging.basicConfig(
    filename='analysis.log',
    level=logging.INFO,
    filemode='w'
)
logger = logging.getLogger("aliya")

logger.info("here is the information")
logger.error("error message goes here")


try:
    age = int(input("enter the age:"))
except Exception as obj:
    logging.error("exceptional details:", exc_info = True)

 



