import argparse


def count_lines(file_path):
    try:
        with open(file_path) as f:
            return len(f.readlines())
    except FileNotFoundError:
        return 0


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--file")
    args = parser.parse_args()

    if args.file:
        print(count_lines(args.file))
