def read() -> list[str]:
    with open("./day1.txt") as f:
        return f.readlines()


def task_one():
    lines = read()
    for line in lines:
        total = 0
        first = ''
        last = ''
        for ch in line:
            if ch.isnumeric():
                if not len(first):
                    first = ch
                last = ch

        total += int(first + last)
        print(total)


def task_two():
    digits = {
        "one": '1',
        "two": '2',
        "three": '3',
        "four": '4',
        "five": '5',
        "six": '6',
        "seven": '7',
        "eight": '8',
        "nine": '9',
    }
    lines = read()
    total = 0
    for line in lines:
        first = ''
        last = ''
        for key, value in digits.items():
            line = line.replace(key, f"{key[0]}{value}{key[-1]}") # replace numbers with actual digit, and add a separator before and after, to avoid conflict
        for ch in line:
            if ch.isnumeric():
                if len(first) == 0:
                    first = ch
                    last = ch
                else:
                    last = ch
        total += int(first + last)         
    print(total)
task_two()  