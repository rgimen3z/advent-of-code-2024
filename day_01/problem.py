from collections import Counter


def parse_file():
    with open('input.txt') as input_file:
        list_1, list_2 = [], []
        for line in input_file.readlines():
            col_1, col_2 = line.split()
            list_1.append(int(col_1))
            list_2.append(int(col_2))

    assert len(list_1) == len(list_2)

    return sorted(list_1), sorted(list_2)


def sum_of_diffs(list_1, list_2):
    total_diff = 0
    for i in range(len(list_1)):
        total_diff += abs(list_1[i] - list_2[i])

    return total_diff


def similarity_score(list_1, list_2):
    counter_2 = Counter(list_2)

    score = 0
    for i in range(len(list_1)):
        number_list_1 = list_1[i]
        times_it_appears_in_2 = counter_2[number_list_1]
        score += number_list_1 * times_it_appears_in_2

    return score




if __name__ == '__main__':
    # Part 1
    list_1, list_2 = parse_file()
    # sum_diff = sum_of_diffs(list_1, list_2)
    # print(sum_diff)

    # Part 2
    print(similarity_score(list_1, list_2))



