import os
import shutil

# Destination folder
destination_dir = r"C:\Users\kayur\OneDrive - University of Cape Town\Map Game\countries"

# Country code to name mapping (partial list; extend as needed)
country_map = {
    "ae": "United Arab Emirates",
    "ao": "Angola",
    "bf": "Burkina Faso",
    "bi": "Burundi",
    "bj": "Benin",
    "bw": "Botswana",
    "cd": "Democratic Republic Congo",
    "cf": "Central African Republic",
    "cg": "Congo",
    "ci": "Côte d'Ivoire",
    "cm": "Cameroon",
    "cv": "Cape Verde",
    "dj": "Djibouti",
    "dz": "Algeria",
    "eg": "Egypt",
    "eh": "Western Sahara",
    "er": "Eritrea",
    "et": "Ethiopia",
    "ga": "Gabon",
    "gh": "Ghana",
    "gm": "Gambia",
    "gn": "Guinea",
    "gq": "Equatorial Guinea",
    "gw": "Guinea-Bissau",
    "ke": "Kenya",
    "km": "Comoros",
    "lr": "Liberia",
    "ls": "Lesotho",
    "ly": "Libya",
    "ma": "Morocco",
    "mg": "Madagascar",
    "ml": "Mali",
    "mr": "Mauritania",
    "mu": "Mauritius",
    "mw": "Malawi",
    "mz": "Mozambique",
    "na": "Namibia",
    "ne": "Niger",
    "ng": "Nigeria",
    "re": "Réunion",
    "rw": "Rwanda",
    "sc": "Seychelles",
    "sd": "Sudan",
    "sh": "Saint Helena, Ascension and Tristan da Cunha",
    "sl": "Sierra Leone",
    "sn": "Senegal",
    "so": "Somalia",
    "ss": "South Sudan",
    "st": "Sao Tome and Principe",
    "sz": "Swaziland",
    "td": "Chad",
    "tg": "Togo",
    "tn": "Tunisia",
    "tz": "Tanzania",
    "ug": "Uganda",
    "yt": "Mayotte",
    "za": "South Africa",
    "zm": "Zambia",
    "zw": "Zimbabwe",
    # Add more mappings as needed
}

# Iterate over subdirectories in current directory
for folder in os.listdir('.'):
    if os.path.isdir(folder):
        country_code = folder.lower()
        country_name = country_map.get(country_code)

        if country_name:
            folder_path = os.path.join('.', folder)
            svg_files = [f for f in os.listdir(folder_path) if f.lower().endswith('.svg')]

            if svg_files:
                svg_file = svg_files[0]  # Assuming only one svg file per folder
                source_path = os.path.join(folder_path, svg_file)
                new_filename = f"{country_name}.svg"
                destination_path = os.path.join(destination_dir, new_filename)

                shutil.move(source_path, destination_path)
                print(f"Moved: {source_path} → {destination_path}")
            else:
                print(f"No SVG found in {folder}")
        else:
            print(f"No country mapping for folder: {folder}")
