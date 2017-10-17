'''contains a class for a month's worth of weather data'''
import urllib
import urllib2
import csv
import datetime

class Month():
  def __init__(self, month, year):
    '''initialises lists, defines names
    month and year should be strings of 3 letter month name and 2 digit year number'''
    self.month = month
    self.year = year
    self.dates = []
    self.times = []
    self.temps = []
    self.rh = [] #relative humidity
    self.windspds = []
    self.winddirs = []
    self.globals = [] #global irradiance
    self.uvas = []
    self.uvbs = []
    self.visibles = []
    self.rain = []
    self.press = []
    self.maxgusts = []
    self.gustimes = []
    self.datetimes = []
  def get_datetimes(self):
    #23:50:00-01/12/2016
    for i, time in enumerate(self.times):
      string = time + '-' + self.dates[i]
      self.datetimes.append(datetime.datetime.strptime(string, "%H:%M:%S-%d/%m/%Y"))
  def get_url(self):
    '''returns url of weather data for month and year of current object.'''
    url = 'http://www.physics.otago.ac.nz/eman/weather_station/weather_data/Archive/' + self.month + '-' +  self.year + '.prn'
    return url
  def get_all_data(self):
    '''loads all weather data into object'''
    url = self.get_url()
    web = urllib2.urlopen(url)
    cr = csv.reader(web, delimiter='\t')
    rownum = 0
    for row in cr:
      # Save header row.
      if rownum == 0:
        header = row
      elif rownum == 1:
        units = row
      elif rownum == 2:
        #discard hyphen row
        pass
      else:
        #print row
        self.dates.append(row[0])
        self.times.append(row[1])
        self.temps.append(float(row[2]))
        self.rh.append(float(row[3])) #relative humidity
        self.windspds.append(float(row[4]))
        self.winddirs.append(float(row[5]))
        self.globals.append(float(row[6]))#global irradiance
        self.uvas.append(float(row[7]))
        self.uvbs.append(float(row[8]))
        self.visibles.append(float(row[9]))
        self.rain.append(float(row[10]))
        self.press.append(float(row[11]))
        self.maxgusts.append(float(row[12]))
        self.gustimes.append(float(row[13]))
      rownum += 1
    web.close()
  def get_temps(self):
    '''loads temperatures into month object'''
    url = self.get_url()
    web = urllib2.urlopen(url)
    cr = csv.reader(web, delimiter='\t')
    rownum = 0
    for row in cr:
      # Save header row.
      if rownum == 0:
        header = row
      elif rownum == 1:
        units = row
      elif rownum == 2:
        #discard hyphen row
        pass
      else:
        #print row
        self.temps.append(float(row[2]))
        #raw_input('paused in reader')
      rownum += 1
    web.close()