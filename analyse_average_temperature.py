'''looks for a linear trend in the average temperatures'''

from year import Year
from visualisation.scattergl_plot import plot_large_scatter
import numpy as np
from sklearn import linear_model
from visualisation.scattergl_plot import plot_two_scatters
from linear_regression_ttest import get_slope_t_statistic, get_two_sided_p_value

#create list of dates in two character string format (corresponds to the format of the web files)
YEARINTS = range(2,17) #years from 2002 to 2016 inclusive
YEARLIST = [str(yr).zfill(2) for yr in YEARINTS] # string format of years

#load all years' data
average_temperatures = []
year_names = []
for year_string in YEARLIST:
  print year_string
  year_object = Year(year_string)
  year_object.load_all_data()
  temperatures = year_object.get_all_temps()
  average_temperatures.append(np.average(temperatures))
  year_names.append(float(year_string) + 2000)
print average_temperatures

# Create linear regression object
regr = linear_model.LinearRegression()
x_values = np.reshape(YEARINTS, (len(YEARINTS), 1))

# Fit the data
regr.fit(x_values, average_temperatures)

# make the best-fit line ("prediction")
y_pred = regr.predict(x_values)
print y_pred

residuals = average_temperatures - y_pred
slope = (y_pred[1] - y_pred[0])/(YEARINTS[1] - YEARINTS[0])
t_value = get_slope_t_statistic(slope, residuals, YEARINTS)
p_value = get_two_sided_p_value(t_value, len(residuals)-2)
print p_value

plot_two_scatters(year_names, average_temperatures, y_pred, 'Date', 'Temperature (C)', 'average_temps')