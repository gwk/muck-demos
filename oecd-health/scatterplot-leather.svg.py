from leather import Chart
from chart_data import rows

chart = Chart('Private Health Care Expenditure vs Life Expectancy')
chart.add_dots([{'x': r.private_cost, 'y': r.expectancy} for r in rows], x='x', y='y')
print('<div>', chart.to_svg(), '</div>', sep='\n') # div is necessary to get block layout.
