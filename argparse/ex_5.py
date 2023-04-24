import argparse

parser = argparse.ArgumentParser()
parser.add_argument("num1", type=int, nargs="?")
parser.add_argument("num2", type=int, nargs="?")


try:
    args = parser.parse_args()
    if args.num1 is None and args.num2 is None:
        print("NO PARAMS")
    elif args.num1 is None or args.num2 is None:
        print("TOO FEW PARAMS")
    else:
        result = args.num1 + args.num2
        print(result)
except SystemExit as e:
    if e.code == 2:
        print("TOO MANY PARAMS")
    else:
        raise
