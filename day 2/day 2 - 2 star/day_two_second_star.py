directory = "./day 2/day 2 - 2 star"
real_bag_composition = {
    "red": 12,
    "green": 13,
    "blue": 14
}


def parse_input(filename: str):
    input_file = open(f"{directory}/{filename}.txt", "r")
    lines = input_file.read().splitlines()
    games_dict = {}
    for game_string in lines:
        game = game_string.split(":")
        sets = game[1][1:].split(";")
        sets_list = []
        for single_set in sets:
            single_colors = single_set.split(", ")
            set_dictionary = {}
            for single_color in single_colors:
                quantity_color = single_color.strip().split(" ")
                quantity = quantity_color[0]
                color = quantity_color[1]
                set_dictionary.update({color: int(quantity)})
            sets_list.append(set_dictionary)
        games_dict.update({game[0]: sets_list})
    return games_dict


def get_power_minimum_set(single_game):
    set_values = {x: 0 for x in real_bag_composition.keys()}
    for single_set in single_game:
        for color, quantity in single_set.items():
            if quantity > set_values.get(color):
                set_values.update({color: quantity})
    prod = 1
    for quantity in set_values.values():
        prod *= quantity
    return prod


def main():
    games_dict = parse_input("input_day2")
    res = sum([get_power_minimum_set(sets) for sets in games_dict.values()])
    print(res)


if __name__ == "__main__":
    main()
