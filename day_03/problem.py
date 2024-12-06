import re


def find_patterns():
    matches = []
    with open('input.txt') as input_file:
        for line in input_file.readlines():
            matches.extend(re.findall(r"mul\(\d{1,3},\d{1,3}\)", line))
    return matches

def mul(x: int, y: int) -> int:
    return x * y

def find_patterns_with_do_and_dont():
    matches = []
    with open('input.txt') as input_file:
        for line in input_file.readlines():
            matches.extend(re.findall(r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)", line))
    return matches

if __name__ == '__main__':
    # Part 1
    matching_patterns = find_patterns()
    total_sum = 0
    for pattern in matching_patterns:
        result = eval(pattern)
        total_sum += result
    print(total_sum)

    # Part 2
    matching_patterns_with_do_and_dont = find_patterns_with_do_and_dont()
    print(matching_patterns_with_do_and_dont)
    total_sum = 0
    do = True
    for pattern in matching_patterns_with_do_and_dont:
        if pattern == "do()":
            do = True
        elif pattern == "don't()":
            do = False
        else:
            if do:
                result = eval(pattern)
                total_sum += result
    print(total_sum)




