import csv

with open('amazon_reviews.csv', newline='', encoding='utf-8') as f:
    reviews = csv.DictReader(f)

    MAX = 1500
    COUNT = 0

    for row in reviews:
        print(row)
        COUNT += 1
        if COUNT == MAX:
            break