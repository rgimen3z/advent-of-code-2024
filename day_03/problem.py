def parse_file():
    file_grid = []
    with open('input.txt') as input_file:
        for line in input_file.readlines():
            file_grid.append(list(line.strip()))

    return file_grid

def count_xmas() -> int:
    grid = parse_file()

    max_x = len(grid[0]) - 1
    max_y = len(grid) - 1

    xmas_counter = 0

    for x in range(max_x + 1):
        for y in range(max_y + 1):
            if grid[x][y] == 'X':
                # we have our starting point, go in all directions
                for direction in [(+1, 0), (+1, +1), (+1, -1), (0, +1), (0, -1), (-1, 0), (-1, +1), (-1, -1)]:
                    x_incr, y_incr = direction
                    new_x, new_y = x + x_incr, y + y_incr
                    if 0 <= new_x <= max_x and 0 <= new_y <= max_y and grid[new_x][new_y] == 'M':
                        # Increase in the same direction and see if the next letter is there
                        new_x = new_x + x_incr
                        new_y = new_y + y_incr
                        if 0 <= new_x <= max_x and 0 <= new_y <= max_y and grid[new_x][new_y] == 'A':
                            # Increase in the same direction and see if the next letter is there
                            new_x = new_x + x_incr
                            new_y = new_y + y_incr
                            if 0 <= new_x <= max_x and 0 <= new_y <= max_y and grid[new_x][new_y] == 'S':
                                xmas_counter += 1

    return xmas_counter


def count_x_mas() -> int:
    """
    This counts:
    M . M
    . A .
    S . S

    But this does not!
    . M .
    S A M
    . S .
    """

    grid = parse_file()

    max_x = len(grid[0]) - 1
    max_y = len(grid) - 1

    xmas_counter = 0

    x_directions = [(+1, +1), (+1, -1), (-1, +1), (-1, -1)]
    opposite_directions = {
        # (+1, 0): (-1, 0),
        # (-1, 0): (+1, 0),
        # (0, +1): (0, -1),
        # (0, -1): (0, +1),
        (+1, +1): (-1, -1),
        (-1, -1): (+1, +1),
        (+1, -1): (-1, +1),
        (-1, +1): (+1, -1),
    }

    for x in range(max_x + 1):
        for y in range(max_y + 1):
            if grid[x][y] == 'A':
                # we have our starting point, go in "X-directions"
                # If we find an 'S', look at opposite end and see if there's an 'M'. Increase counter if so.
                # We don't need to do it the other way around (look for 'M' and check if opposite is 'S') or we'd
                # double-count.
                counter_for_current_a = 0

                for direction in x_directions:
                    x_incr, y_incr = direction
                    new_x, new_y = x + x_incr, y + y_incr
                    if 0 <= new_x <= max_x and 0 <= new_y <= max_y and grid[new_x][new_y] == 'S':
                        opposite_dir_increment_x, opposite_dir_increment_y = opposite_directions[direction]
                        opposite_x, opposite_y = x + opposite_dir_increment_x, y + opposite_dir_increment_y
                        if 0 <= opposite_x <= max_x and 0 <= opposite_y <= max_y and grid[opposite_x][opposite_y] == 'M':
                            counter_for_current_a += 1

                if counter_for_current_a >= 2:
                    xmas_counter += 1

    return xmas_counter


if __name__ == '__main__':
    # Part 1
    print(count_xmas())

    # Part 2
    print(count_x_mas())



