import csv
from itertools import islice
import matplotlib.pyplot as plt

scores = []
dates = []

with open('amazon_reviews.csv', newline='', encoding='utf-8') as f:
    reviews = csv.DictReader(f)

    for row in islice(reviews, 1500):
        scores.append(float(row['thumbsUpCount']))
        dates.append(row['at'])

fig, ax = plt.subplots()
ax.plot(dates, scores)

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()