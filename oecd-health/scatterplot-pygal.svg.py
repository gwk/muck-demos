from pygal import Config, XY
from chart_data import rows

config = Config()
config.show_legend = False
config.human_readable = True
chart = XY(config, print_labels=True, show_y_guides=False, stroke=False)
chart.title = 'Private Health Care Expenditure vs Life Expectancy'

def point_from(row):
  return {
    'value': (row.total_cost, row.expectancy),
    'label': row.country,
    'formatter': lambda v: f'${v[0]} : {v[1]} years'
  }

chart.add('', [point_from(row) for row in rows])
print(chart.render(is_unicode=True))
