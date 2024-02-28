import re
literal_to_numbers = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}

def parse_input(filename: str):
    input_file = open(f"./day 1/day 1 - 2 star/{filename}.txt", "r")
    return [line for line in input_file]


def get_line_sum(line: str):
    counter=0
    numbers=[]
    regex_string= "^("+"|".join(literal_to_numbers.keys())+")"
    while(counter < len(line)):
        if (line[counter].isnumeric()):
            numbers.append(int(line[counter]))
            counter+=1
        else:
            match=re.search(regex_string,line[counter:])
            if (match):
                numbers.append(int(literal_to_numbers.get(match.group())))
                counter+=len(match.group())-1
            else:
                counter+=1
    return numbers[0]*10+numbers[-1]


def get_total_sum(lines: list):
    return sum([get_line_sum(line) for line in lines])


def main():
    lines = parse_input("input_day1_second")
    res = get_total_sum(lines)
    print(res)


if __name__ == "__main__":
    main()
