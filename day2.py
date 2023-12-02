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
        line = line.split(": ")
        game_id = list(map(lambda y: int(y) if y.isdigit()
                    else None, line[0].split(' ')))[1]
        line = line[1].split("; ")
        impossible = False
        for game in line:
            game = tuple(map(lambda x: x.split(' '), game.split(', ')))
            for round in game:
                if max_values[round[1]] < int(round[0]):
                    impossible = True
                    break
        if not impossible:
            id_sum += game_id
    print(id_sum)


def task_two():
    lines = read()
    powers = []
    for line in lines:
        line = line.split(": ")
        max_values = {
            "red": 0,
            "green": 0,
            "blue": 0,
        }
        line = line[1].split("; ")
        for game in line:
            game = tuple(map(lambda x: x.split(' '), game.split(', ')))
            for round in game:
                number = int(round[0])
                color = round[1]
                if number > max_values[color]:
                    max_values[color] = number
        total = 1
        for val in max_values.values():
            total *= val
        powers.append(total)
    print(sum(powers))


task_two()
