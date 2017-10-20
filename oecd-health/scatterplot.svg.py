from xml.etree.ElementTree import Element
from muck import *
from leather import Chart, Series, Dots
from chart_data import rows


class TitledDots(Dots):
  'Hack to get tooltips (SVG title elements) into dot plots.'
  def to_svg(self, width, height, x_scale, y_scale, series, palette):
    group = super().to_svg(width, height, x_scale, y_scale, series, palette)
    for datum, circle in zip(series.data(), group.findall('circle')):
      title = Element('title')
      title.text = datum.row['title']
      circle.append(title)
    return group


chart = Chart('Private Health Care Expenditure vs Life Expectancy')
chart.add_series(
  Series([{'x': r.private_cost, 'y': r.expectancy, 'title': r.country} for r in rows], x='x', y='y', name='Private Expenditure'),
  TitledDots(fill_color='black', radius='4'))
chart.add_series(
  Series([{'x': r.total_cost, 'y': r.expectancy, 'title': r.country} for r in rows], x='x', y='y', name='Total Expenditure'),
  TitledDots(fill_color='#C00000', radius='4'))

print('<div>', chart.to_svg(), '</div>', sep='\n') # div is necessary to get block layout.
