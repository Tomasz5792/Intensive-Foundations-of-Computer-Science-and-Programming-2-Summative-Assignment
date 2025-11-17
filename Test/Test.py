import csv

with open("table_data.csv", newline='', encoding='utf-8') as f:
    reader = csv.reader(f)
    rows = list(reader)

if rows:
    columns = rows[0]
    data = rows[1:]

print(columns)
print(data)