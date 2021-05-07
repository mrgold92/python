from datetime import datetime, timedelta
from pytz import timezone
import pytz

#----------------------------------------------------------------#
# pytz.all_timezones devuelve todas las zonas horarias.
# datetime.now(timezone('zona')) devuelve la fecha de la zona.
#----------------------------------------------------------------#

# print(pytz.all_timezones)
print(datetime.now(timezone('Asia/Tokyo')))
print(datetime.now(timezone('Europe/Madrid')))
print(datetime.now(timezone('US/Alaska')))
print(datetime.now(timezone('UTC')))
