from muck import load
from collections import Counter
from pithy.json_utils import out_json


data = load('climate-comments-data.json')['data']

counter = Counter()
aux = {}
for record in data:
  ( sid, id, position, created_at, created_meta, updated_at, updated_meta,
    meta, name, affiliation, home_town, state_or_country, comment, attachment) = record
  counter[comment] += 1
  aux.setdefault(comment, (name, affiliation, home_town, state_or_country))

out_json(sorted([(count, comment) + aux[comment] for (comment, count) in counter.items()], reverse=True))
