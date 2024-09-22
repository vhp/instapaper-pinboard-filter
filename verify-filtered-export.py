#!/usr/bin/env python3
# Use to verify your filtered_instapaper_export.csv. This should catch case difference issues in urls.
import csv
import json
from urllib.parse import unquote

filtered_instapaper_csv_file_path = 'filtered_instapaper_export.csv'
pinboard_json_file_path = 'pinboard_export.2024.09.16_02.47.json'

pinboard_urls = set()
matching_urls = []
quoted_matching_urls = []

with open(pinboard_json_file_path, 'r', encoding='utf-8') as jsonfile:
    pinboard_data = json.load(jsonfile)
    for entry in pinboard_data:
        pinboard_urls.add(unquote(entry['href'].lower()))

with open(filtered_instapaper_csv_file_path, mode='r', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)

    for row in reader:
         if unquote(row['URL'].lower()) in pinboard_urls:
            matching_urls.append(row['URL'].lower())

        if row['URL'].lower() in pinboard_urls:
            quoted_matching_urls.append(row['URL'].lower())

if matching_urls:
    print("Matching URLs in the filtered Instapaper file:")
    for url in matching_urls:
        print(url)
else:
    print("No duplicate/matching URLs found in the filtered Instapaper file.")

if quoted_matching_urls:
    print("Found non escaped matching_urls in the filtered Instapaper file:")
    for url in quoted_matching_urls:
        print(url)
else:
    print("No unescaped matching URLs found in the filtered Instapaper file.")

