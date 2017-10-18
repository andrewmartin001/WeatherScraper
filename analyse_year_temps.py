'''script to scrape and plot the temperatures for the year to date (2017)'''

from year import Year
from visualisation.scattergl_plot import plot_large_scatter

#plot temperatures of year to date (2017)
#initiate a 'year object' and load the data from the web
yeartwelve = Year('17')
yeartwelve.load_all_data()

#assign the temperature and date data into variables yeartemps and yeartimes
yeartemps = yeartwelve.get_all_temps()
yeartimes = yeartwelve.get_all_datetimes()

#plot using plotly
plot_large_scatter(yeartimes, yeartemps, 'Date', 'Temperature (C)', 'yeartemps')

