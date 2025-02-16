import datetime

class defDate:
    def __init__(self, date):
        self.date = datetime.timedelta(days = date)
        self.today = datetime.datetime.now()
    def secsdelta(self):
        date1 = self.today - self.date
        delta = self.today - date1        
        return delta.total_seconds()

date = defDate(int(input('Enter a date:\n')))
print(date.secsdelta())