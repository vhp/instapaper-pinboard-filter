#!/usr/bin/env python3
# Rough script that filters out urls in your pinboard export from your instapaper-export.csv.
# * Fill in your filesnames below.
# Use verify script to double check.
# Limitations:
# - Similar urls with case differences can get through detection.
import csv
import json
from urllib.parse import unquote

instapaper_csv_file_path = 'instapaper-export.csv'
pinboard_json_file_path = 'pinboard_export.2024.09.16_02.47.json'
output_csv_file_path = 'filtered_instapaper_export.csv'

pinboard_urls = set()
filtered_rows = []

with open(pinboard_json_file_path, 'r', encoding='utf-8') as jsonfile:
    pinboard_data = json.load(jsonfile)
    for entry in pinboard_data:
        pinboard_urls.add(unquote(entry['href']))

with open(instapaper_csv_file_path, mode='r', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)

    for row in reader:
        instapaper_url = unquote(row['URL'])
        if instapaper_url not in pinboard_urls:
            filtered_rows.append(row)


with open(output_csv_file_path, mode='w', encoding='utf-8', newline='') as csvfile:
    fieldnames = ['URL', 'Title', 'Selection', 'Folder', 'Timestamp']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(filtered_rows)

print(f"Writing out {output_csv_file_path} filtered entries.")
print(f"Filtered entries count: {len(filtered_rows)}")
