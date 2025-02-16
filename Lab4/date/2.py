from datetime import *

yesterday = date.today() - timedelta(days = 1)
today = date.today()
tommorow = date.today() + timedelta(days = 1)
print(yesterday,",", today,",", tommorow)