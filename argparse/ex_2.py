import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--barbie', type=int, default=50)
parser.add_argument('--cars', type=int, default=50)
parser.add_argument('--movie', choices=['melodrama', 'football', 'other'], default='other')
args = parser.parse_args()

if args.movie == 'melodrama':
    movie_value = 0
elif args.movie == 'football':
    movie_value = 100
else:
    movie_value = 50

if args.barbie > 100 or args.barbie < 0:
    args.barbie = 50
if args.cars > 100 or args.cars < 0:
    args.cars = 50

boy = (100 - args.barbie + args.cars + movie_value) // 3
girl = 100 - boy

print(f'boy: {boy}')
print(f'girl: {girl}')
