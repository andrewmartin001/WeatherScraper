'''An object for a year's-worth of weather data'''
from month import Month

MONTHLIST = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

class Year():
  def __init__(self, year_no):
    '''initialise year number (last two digits of year), and month dict (empty of weather data)'''
    self.year_no = year_no
    self.months = {}
    for month_string in MONTHLIST:
      month_object = Month(month_string, self.year_no)
      self.months[month_string] = month_object
  def load_all_data(self):
    '''puts data in for each month of the year'''
    for month_string in MONTHLIST:
      try:
        month_object = self.months[month_string]
        month_object.get_all_data()
      except Exception as e:
        print 'exception in month %s year %s' %(month_string, str(self.year_no))
        print e
  def get_all_temps(self):
    '''puts all temperatures from the year into a list'''
    temps = []
    for month_string in MONTHLIST:
      try:
        month_object = self.months[month_string]
        temps.extend(month_object.temps)
      except Exception as e:
        print 'exception in getting temp from month %s year %s' %(month_string, str(self.year_no))
        print e
    return temps
  def get_all_rainfall(self):
    '''puts all rainfall from the year into a list'''
    rain = []
    for month_string in MONTHLIST:
      try:
        month_object = self.months[month_string]
        rain.extend(month_object.rain)
      except Exception as e:
        print 'exception in getting temp from month %s year %s' %(month_string, str(self.year_no))
        print e
    return rain
  def get_all_datetimes(self):
    times = []
    for month_string in MONTHLIST:
      try:
        month_object = self.months[month_string]
        month_object.get_datetimes()
        times.extend(month_object.datetimes)
      except Exception as e:
        print 'exception in getting times from month %s year %s' %(month_string, str(self.year_no))
        print e
    return times

