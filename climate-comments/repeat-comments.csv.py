from muck import load
from pithy.csv_utils import out_csv


rows = load('comment-counts.json')
repeated = [row[:2] for row in rows if row[0] > 1]
out_csv(header=('Count', 'Comment Text'), rows=repeated)
