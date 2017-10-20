from muck import *
from typing import NamedTuple

header = ('Country', 'Private Cost', 'Total Cost', 'Life Expectancy', 'LE Year')

class Row(NamedTuple):
  country: str
  private_cost: float
  total_cost: float
  expectancy: float
  le_year: int

with load('table.csv', header=header) as reader:
  rows = [Row(c, float(p), float(t), float(e), int(y)) for c, p, t, e, y in reader]
