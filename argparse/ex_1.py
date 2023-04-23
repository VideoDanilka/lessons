import argparse

parser = argparse.ArgumentParser(add_help=False)
parser.add_argument('args', nargs='*', help=argparse.SUPPRESS)
args = parser.parse_args()

if not args.args:
    print('no args')
else:
    for arg in args.args:
        print(arg)
