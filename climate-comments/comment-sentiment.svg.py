from muck import load
from collections import Counter
from textblob import TextBlob
from pithy.io import *
from hearts import *


rows = load('comment-counts.json')
sentiments = Counter()
for row in rows:
  comment_count, comment = row[:2]
  blob = TextBlob(comment)
  polarity = blob.sentiment.polarity
  sentiments[round(polarity * 20)] += 1

chart = Chart(title='Comment Sentiment Histogram',
  axes=[Axis('Sentiment Score (20ths)'), Axis('# of Comments')])

errP(sentiments)
chart.add(Bars(sentiments.items()))
outZ(chart.to_svg())

