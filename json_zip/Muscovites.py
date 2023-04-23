import zipfile
import json

zip_filename = "input.zip"
moscow_count = 0

with zipfile.ZipFile(zip_filename) as zip_file:
    for file_info in zip_file.infolist():
        if file_info.filename.endswith(".json"):
            with zip_file.open(file_info) as json_file:
                data = json.load(json_file)
                if data["city"] == "Moscow":
                    moscow_count += 1

print(moscow_count)
