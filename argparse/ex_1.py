import argparse

parser = argparse.ArgumentParser()
parser.add_argument('arg', nargs='*', help='')
args = parser.parse_args()

if not args.arg:
    print('no args')
else:
    for arg in args.arg:
        print(arg)
