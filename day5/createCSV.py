import csv

with open('day5/demo.csv', 'w', newline="") as f:
    fieldName = ['column1', 'column2', 'column3']
    writer = csv.DictWriter(f, fieldnames=fieldName)
    writer.writeheader()
    writer.writerow({'column1': 'abc', 'column2': 'def', 'column3': 'adsfvgq'})
