import sys

# проверяем, что передан аргумент с именем файла
filename = ''
if len(sys.argv) <= 0:
    print("ERROR")
    sys.exit()
elif len(sys.argv) == 2:
    filename = sys.argv[1]
elif len(sys.argv) == 3:
    filename = sys.argv[2]
elif len(sys.argv) == 4:
    filename = sys.argv[3]
elif len(sys.argv) == 5:
    filename = sys.argv[4]

# проверяем, что файл существует
try:
    with open(filename, 'r') as file:
        lines = file.readlines()
except FileNotFoundError:
    print("ERROR")
    sys.exit()

# обработка дополнительных аргументов
sort_lines = False
numbered_lines = False
count_lines = False

for arg in sys.argv[1:]:
    if arg == '--sort':
        sort_lines = True
    elif arg == '--num':
        numbered_lines = True
    elif arg == '--count':
        count_lines = True

# сортировка строк
if sort_lines:
    lines.sort()

# вывод строк
if numbered_lines:
    for i, line in enumerate(lines):
        print(f"{i} {line}", end='')
else:
    for line in lines:
        print(line, end='')

# вывод кол-ва строк
if count_lines:
    print(f"rows count: {len(lines)}")
