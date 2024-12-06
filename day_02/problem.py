from collections import Counter


def is_valid_sequence(sequence: list[int]):
    """
    Valid if always increasing or always decreasing AND it always increases/decreases by at least 1 and at most 3.
    """
    prev = sequence[0]
    increasing = sequence[0] < sequence[1]

    for current in sequence[1:]:
        if current == prev:
            return False  # didn't change at all.

        if prev < current and not increasing:
            return False  # it increased when it wasn't supposed to

        if prev > current and increasing:
            return False  # in decreased when ti wasn't supposed to

        if abs(current - prev) > 3:
            return False  # it changed by too much

        prev = current

    return True

def is_valid_sequence_with_tolerance(sequence: list[int], tolerance_level: int):
    if tolerance_level > 1:
        # Removed more than one element
        return False

    # increasing = True  # we may need to adjust this to account for removing the first or second value

    prev_i, prev_prev_i = 0, 0

    for i, curr in enumerate(sequence):
        if i == 0:
            continue

        prev_prev = sequence[prev_prev_i]
        prev = sequence[prev_i]

        if curr != prev:  # different
            if (prev_prev <= prev <= curr) or (prev_prev >= prev >= curr):  # increasing or decreasing
                if abs(curr - prev) <= 3:  # too big of a gap
                    prev_prev_i = prev_i
                    prev_i = i
                    continue

        # Otherwise, we ran into an issue, check removing prev_prev, prev, or current.
        sequence_minus_prev_prev = sequence[:prev_prev_i] + sequence[prev_prev_i + 1:]
        sequence_minus_prev = sequence[:prev_i] + sequence[prev_i + 1:]
        sequence_minus_curr = sequence[:i] + sequence[i + 1:]
        return (
                is_valid_sequence_with_tolerance(sequence_minus_prev_prev, tolerance_level + 1)
                or is_valid_sequence_with_tolerance(sequence_minus_prev, tolerance_level + 1)
                or is_valid_sequence_with_tolerance(sequence_minus_curr, tolerance_level + 1)
        )

    return True


def count_valid_sequences():
    with open('input.txt') as input_file:
        valid_counter = 0
        for line in input_file.readlines():
            sequence = [int(char) for char in line.split()]
            if is_valid_sequence(sequence):
                valid_counter += 1

    return valid_counter


def count_valid_sequences_with_tolerance():
    with open('input.txt') as input_file:
        valid_counter = 0
        for line in input_file.readlines():
            sequence = [int(char) for char in line.split()]
            if is_valid_sequence_with_tolerance(sequence, 0):
                valid_counter += 1
            else:
                print(f"Invalid sequence: {line}")

    return valid_counter


if __name__ == '__main__':
    # Part 1
    valid_sequences = count_valid_sequences()
    print(valid_sequences)

    # Part 2
    valid_sequences_with_tolerance = count_valid_sequences_with_tolerance()
    print(valid_sequences_with_tolerance)




