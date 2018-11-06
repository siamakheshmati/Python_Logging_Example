import logging
from datetime import datetime

now="{:%Y-%m-%d %H:%M}".format(datetime.now())
logging.basicConfig(filename='applog.log',level=logging.INFO)
logging.info('\n\n************************')
logging.info('app started ' +  ' || '+ now)

for i in  range(5):
    
    try:
        print i/0
    except ZeroDivisionError:
        logging.error('Devide by zero!'  +  ' || ' + now)
        pass


   
logging.info('app completed successfuly')

