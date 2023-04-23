import argparse

parser = argparse.ArgumentParser()

parser.add_argument('--per-day', type=float, default=0)
parser.add_argument('--per-week', type=float, default=0)
parser.add_argument('--per-month', type=float, default=0)
parser.add_argument('--per-year', type=float, default=0)

parser.add_argument('--get-by', choices=['day', 'month', 'year'], default='day')

args = parser.parse_args()

if args.get_by == 'day':
    result = int(args.per_day + args.per_week / 7 + args.per_month / 30 + args.per_year / 360)
elif args.get_by == 'month':
    result = int(args.per_day * 28 + args.per_week * 4 + args.per_month + args.per_year / 12)
else:
    result = int(args.per_day * 360 + args.per_week * 52 + args.per_month * 12 + args.per_year)

print(result)
