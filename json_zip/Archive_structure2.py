import zipfile


def human_readable_size(size, decimal_places=2):
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if size < 1024.0:
            break
        size /= 1024.0
    return f"{size:.{decimal_places}f} {unit}"


zip_file = "input.zip"

if not zipfile.is_zipfile(zip_file):
    print(f"{zip_file} is not a valid zip file.")
    exit()

with zipfile.ZipFile(zip_file, "r") as zf:
    for file_info in zf.infolist():
        path_parts = file_info.filename.split("/")
        depth = len(path_parts) - 1
        filename = path_parts[-1]
        if filename:
            size = human_readable_size(file_info.file_size)
            print(f"{'  ' * depth}{filename} {size}")
