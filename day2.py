def read():
    with open("./day2.txt") as f:
        return [l.strip() for l in f.readlines()]


def task_one():
    lines = read()
    max_values = {
        "red": 12,
        "green": 13,
        "blue": 14
    }
    id_sum = 0
    for line in lines:
        line = line.split(": ") #split game metadada and game data
        game_id = list(map(lambda y: int(y) if y.isdigit()
                    else None, line[0].split(' ')))[1]# get game id 
        line = line[1].split("; ")# get data of each round
        impossible = False
        for game in line:
            game = tuple(map(lambda x: x.split(' '), game.split(', '))) # get [1] color and [0] number data
            for round in game:
                if max_values[round[1]] < int(round[0]): # check whether the numbers are too high
                    impossible = True
                    break
        if not impossible:
            id_sum += game_id
    print(id_sum)


def task_two():
    lines = read()
    powers = []
    for line in lines:
        line = line.split(": ") # separate game metadata and round data
        max_values = {
            "red": 0,
            "green": 0,
            "blue": 0,
        }
        line = line[1].split("; ") # separate each round
        for game in line:
            game = tuple(map(lambda x: x.split(' '), game.split(', '))) # get color/number data
            for round in game:
                number = int(round[0])
                color = round[1]
                if number > max_values[color]: #check whether it's the maximum value
                    max_values[color] = number
        total = 1
        for val in max_values.values():
            total *= val
        powers.append(total)
    print(sum(powers))


task_two()
