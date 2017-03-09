from muck import load
from pithy.io import *

meta = muck.load('climate-comments-data.json')['meta']
columns = meta['view']['columns']
outL([c['fieldName'] for c in columns])
