directory = "./day 2/day 2 - 1 star"
real_bag_composition= {
    "red":12,
    "green":13,
    "blue":14
}

def parse_input(filename: str):
    input_file = open(f"{directory}/{filename}.txt", "r")
    lines = input_file.read().splitlines()
    games_dict = {}
    for game_string in lines:
        game = game_string.split(":")
        sets = game[1][1:].split(";")
        sets_list= []
        for single_set in sets:
            single_colors= single_set.split(", ")
            set_dictionary={}
            for single_color in single_colors:
                quantity_color=single_color.strip().split(" ")
                quantity= quantity_color[0]
                color=quantity_color[1]
                set_dictionary.update({color:int(quantity)})
            sets_list.append(set_dictionary)
        games_dict.update({game[0]: sets_list})
    return games_dict

def check_game(single_game):
    for single_set in single_game:
        for color,max_value in real_bag_composition.items():
            if (single_set.get(color,0) > max_value):
                return False
    return True

def main():
    games_dict = parse_input("input_day2")
    res=0
    for game,sets in games_dict.items():
        if (check_game(sets)):
            res +=int(game.replace("Game ",""))
    print(res)
if __name__ == "__main__":
    main()
