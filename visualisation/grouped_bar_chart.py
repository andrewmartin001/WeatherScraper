import plotly.plotly as py
import plotly.graph_objs as go


def grouped_bar_chart():
  trace1 = go.Bar(
      x=['giraffes', 'orangutans', 'monkeys'],
      y=[20, 14, 23],
      name='SF Zoo'
  )
  trace2 = go.Bar(
      x=['giraffes', 'orangutans', 'monkeys'],
      y=[32, 18, 29],
      name='LA Zoo'
  )

  data = [trace1, trace2]
  layout = go.Layout(
      barmode='group'
  )

  fig = go.Figure(data=data, layout=layout)
  py.plot(fig, filename='grouped-bar')

if __name__ == '__main__':
  grouped_bar_chart()
