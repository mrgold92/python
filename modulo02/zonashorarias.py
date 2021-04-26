from datetime import datetime, timedelta
from pytz import timezone
import pytz

#----------------------------------------------------------------#
# pytz.all_timezones devuelve todas las zonas horarias.
# datetime.now(pytz.timezone('zona')) devuelve la fecha de la zona.
#----------------------------------------------------------------#

print(pytz.all_timezones)
print(datetime.now(pytz.timezone('Asia/Tokyo')))
print(datetime.now(pytz.timezone('Europe/Madrid')))
