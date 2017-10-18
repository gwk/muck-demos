from muck import *
from typing import NamedTuple


header = ('Country', 'Private Cost', 'Total Cost', 'Life Expectancy')

class Row(NamedTuple):
  country: str
  private_cost: float
  total_cost: float
  expectancy: float

rows = [Row(c, float(p), float(t), float(e)) for c, p, t, e in load('table.csv', header=header)]
