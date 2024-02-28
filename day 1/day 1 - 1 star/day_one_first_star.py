
import re


def parse_input(filename: str):
    input_file = open(f"./day 1/day 1 - 1 star/{filename}.txt", "r")
    return [line for line in input_file]


def get_line_sum(line: str):
    numbers = re.findall("\d", line)
    return int(numbers[0])*10+int(numbers[-1])


def get_total_sum(lines: list):
    return sum([get_line_sum(line) for line in lines])


def main():
    lines = parse_input("input_day1")
    print(get_total_sum(lines))


if __name__ == "__main__":
    main()
