from muck import load
from pithy.csv_utils import out_csv


rows = load('comment-counts.json')
uniques = sorted((row[1:] for row in rows), key=lambda r: str(r[1:]))
out_csv(header=('Comment Text', 'Name', 'Affiliation', 'Town', 'State'), rows=uniques)
