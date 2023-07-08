import logging

#Example 1
logging.debug('This is a debug message')
logging.info('This is an info message')
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical message')

#Example 2
logging.basicConfig(level=logging.WARNING)

logging.debug('This message will not be logged')
logging.warning('This is a warning message')
logging.error('This is an error message')