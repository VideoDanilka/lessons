import argparse

parser = argparse.ArgumentParser(description='Read file content with optional arguments')
parser.add_argument('filename', metavar='FILENAME', type=str, help='name of the file to read')
parser.add_argument('--count', action='store_true', help='display number of lines')
parser.add_argument('--num', action='store_true', help='display line numbers')
parser.add_argument('--sort', action='store_true', help='sort lines alphabetically')

args = parser.parse_args()

try:
    with open(args.filename, 'r') as file:
        lines = file.readlines()
        if args.sort:
            lines.sort()
        if args.num:
            for i, line in enumerate(lines):
                line = str.strip(line)
                print(f"{i} {line}")
        else:
            for line in lines:
                line = str.strip(line)
                print(line)
    if args.count:
        print(f"rows count: {len(lines)}")
except FileNotFoundError:
    print('ERROR')
