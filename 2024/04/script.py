with open("data_example.dat", "r") as f:
    example_data = f.read().splitlines()
    example_data = [list(line) for line in example_data]

with open("data.dat", "r") as f:
    data = f.read().splitlines()
    data = [list(line) for line in data]


def walk_grid(grid:list[list[str]], x: int, y: int) -> int:
    '''
    We know where to start and the string we are looking for.
    Move in the 8 directions to see if we find it.

    :param grid: The grid to be search
    :param x: starting row
    :param y: starting column
    :return: how many were found?
    '''
    XMAS = 'XMAS'

    count: int = 0
    vectors = [
        (1, 0),
        (1, 1),
        (0, 1),
        (-1, 1),
        (-1, 0),
        (-1, -1),
        (0, -1),
        (1, -1)
    ]
    for v in vectors:
        change_y, change_x = y+v[0]*3, x+v[1]*3
        if 0 <= change_y < len(grid) and 0 <= change_x < len(grid[0]):
            test_string: str = "".join([
                grid[y][x],
                grid[y + v[0]][x + v[1]],
                grid[y + v[0]*2][x + v[1]*2],
                grid[y + v[0]*3][x + v[1]*3]
            ])
            if test_string == XMAS:
                count += 1
    return count

def square_search(grid:list[list[str]], x:int, y:int) -> list[list[str]]:
    '''
    Find the Grid based on the 'A'

    We can ignore the first and last of each row/column, because that doesn't leave enough
    room for a square.

    :param grid: The grid to be search
    :param grid: The grid to be search
    :param x: starting row
    :param y: starting column
    :return: square representation
    '''
    square: list = [[True,False,True],[False,True,False],[True,False,True]]
    vectors = [
        [(1, -1), (1, 0), (1, 1)],
        [(0, -1), (0, 0), (0, 1)],
        [(-1, -1), (-1, 0), (-1, 1)]
    ]
    for v_y in range(len(vectors)):
        for v_x in range(len(vectors[v_y])):
            if square[v_y][v_x]:
                letter = grid[y+vectors[v_y][v_x][0]][x+vectors[v_y][v_x][1]]
                if letter in ['M', 'A', 'S']:
                    square[v_y][v_x] = letter
                else:
                    # there is a letter in the 'X' that does not belong
                    return None
            else:
                # makes the square easier to debug.
                square[v_y][v_x] = ''
    return square

def square_test(square:list[list[str]])-> int:
    mas_one = f"{square[0][0]}{square[1][1]}{square[2][2]}"
    mas_two = f"{square[0][2]}{square[1][1]}{square[2][0]}"
    if (
            (mas_one == 'MAS'
            or mas_one[::-1] == 'MAS')
            and (mas_two == 'MAS'
            or mas_two[::-1] == 'MAS')
    ):
        return 1

    return 0

def part_one(search_grid: list[list[str]]) -> int:
    count: int = 0
    for y in range(len(search_grid)):
        row = search_grid[y]
        for x in range(len(row)):
            letter = row[x]
            if letter == "X":
                count += walk_grid(search_grid, x, y)
    return count

assert(part_one(example_data) == 18)
print(f"PART ONE COUNT TOTAL:{part_one(data)}")


def part_two(search_grid: list[list[str]]) -> int:
    count: int = 0
    for y in range(1, len(search_grid)-1):
        row = search_grid[y]
        for x in range(1, len(row)-1):
            letter = row[x]
            if letter == "A":
                if square := square_search(search_grid, x, y):
                    count += square_test(square)
    return count

assert(part_two(example_data) == 9)
print(f"PART TWO COUNT TOTAL:{part_two(data)}")
