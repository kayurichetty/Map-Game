import os
import json

# Define the path to the folder
folder_path = r"C:\Users\kayur\OneDrive - University of Cape Town\Map Game\countries"

# Get all filenames (including extensions) from the folder
country_files = []
for filename in os.listdir(folder_path):
    full_path = os.path.join(folder_path, filename)
    if os.path.isfile(full_path):
        country_files.append(filename)

# Write to countries.json in the same folder
json_path = os.path.join(folder_path, "countries.json")
with open(json_path, "w", encoding="utf-8") as f:
    json.dump(country_files, f, indent=4)

print(f"Saved {len(country_files)} country filenames to {json_path}")
