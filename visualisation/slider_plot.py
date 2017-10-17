import plotly.plotly as py
import plotly.graph_objs as go 

from datetime import datetime
import pandas_datareader.data as web

#df = web.DataReader("aapl", 'yahoo',
#                    datetime(2007, 10, 1),
#                    datetime(2009, 4, 1))

def plot_slider(x_data, y_data, x_title, y_title, filename):
    '''plots a scatter plot'''
    trace = go.Scatter(x=x_data,
                       y=y_data)

    data = [trace]
    layout = dict(
        xaxis=dict(
            title=x_title,
            rangeselector=dict(
                buttons=list([
                    dict(count=1,
                         label='1m',
                         step='month',
                         stepmode='backward'),
                    dict(count=6,
                         label='6m',
                         step='month',
                         stepmode='backward'),
                    dict(count=1,
                        label='YTD',
                        step='year',
                        stepmode='todate'),
                    dict(count=1,
                        label='1y',
                        step='year',
                        stepmode='backward'),
                    dict(step='all')
                ])
            ),
            rangeslider=dict(),
            type='date'
        ),
        yaxis=dict(
            title=y_title
        )
    )
    fig = dict(data=data, layout=layout)
    py.plot(fig, filename = filename)