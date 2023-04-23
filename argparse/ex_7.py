import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--sort", action="store_true", help="Sort output by key")
parser.add_argument("params", nargs="*", help="List of key=value parameters")

args = parser.parse_args()

params_dict = {}
for param in args.params:
    key, value = param.split("=")
    params_dict[key] = value

if args.sort:
    sorted_keys = sorted(params_dict.keys())
    for key in sorted_keys:
        print(f"Key: {key}\tValue: {params_dict[key]}")
else:
    for key, value in params_dict.items():
        print(f"Key: {key}\tValue: {value}")
