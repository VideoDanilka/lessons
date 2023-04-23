import sys

args = sys.argv[1:]
sort_flag = False

# Проверяем наличие опции --sort
if "--sort" in args:
    sort_flag = True
    args.remove("--sort")

# Если опция --sort задана, сортируем аргументы по ключу
if sort_flag:
    args.sort(key=lambda x: x.split("=")[0])

# Выводим ключи и значения аргументов
for arg in args:
    key, value = arg.split("=")
    print("Key:", key, "Value:", value)
