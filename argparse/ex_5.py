import argparse

parser = argparse.ArgumentParser(description='Sum two integer arguments')
parser.add_argument('arg1', nargs='?', type=int, help='First integer argument')
parser.add_argument('arg2', nargs='?', type=int, help='Second integer argument')
args = parser.parse_args()

if args.arg1 is None and args.arg2 is None:
    print('NO PARAMS')
elif args.arg1 is None or args.arg2 is None:
    print('TOO FEW PARAMS')
elif len(vars(args)) > 2:
    print('TOO MANY PARAMS')
else:

    result = args.arg1 + args.arg2
    print(result)
    print(len(vars(args)))
