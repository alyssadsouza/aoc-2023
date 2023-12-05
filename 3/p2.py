from math import prod

############# Part 2 #############


def getNumberFromDigitAtPos(row: int, col: int, grid: list[list]) -> int:
    """
    Returns a list: first item is a whole number from the schematics given a single digit at specified position
    Subsequent items are the grid positions of all the number's digits
    """
    num, positions = "", []
    # get to the start of the number (leftmost digit)
    while col - 1 >= 0 and grid[row][col - 1].isdigit():
        col -= 1
    # get each digit one at a time left to right
    while col < len(grid[row]) and grid[row][col].isdigit():
        num += grid[row][col]
        positions.append((row, col))
        col += 1

    return [int(num)] + positions


def isDigitAtPos(row: int, col: int, grid: list[list]) -> bool:
    """Determines if specified position is valid in the grid and contains a digit"""
    return 0 <= row < len(grid) and 0 <= col < len(grid[row]) and grid[row][col].isdigit()


def getAdjacentNums(row: int, col: int, grid: list[list]) -> list[int]:
    """Gets all numbers adjacent to current position"""
    adjacentPositions = [
        (row-1, col),  # top
        (row-1, col+1),  # top right
        (row, col+1),  # right
        (row+1, col+1),  # bottom right
        (row+1, col),  # bottom
        (row+1, col-1),  # bottom left
        (row, col-1),  # left
        (row-1, col-1),  # top left
    ]
    adjacentNums = []
    while len(adjacentPositions) > 0:
        y, x = adjacentPositions[0]
        if isDigitAtPos(y, x, grid):
            numAndPositions = getNumberFromDigitAtPos(y, x, grid)
            adjacentNums.append(numAndPositions[0])
            adjacentPositions = [pos for pos in adjacentPositions if pos not in numAndPositions[1:]]
        else:
            adjacentPositions.pop(0)
    return adjacentNums


def getGearRatio(row: int, col: int, grid: list[list]) -> bool:
    """Determines if specified position has a gear and returns gear ratio, else returns 0"""
    if grid[row][col] == "*":
        adjacentNums = getAdjacentNums(row, col, grid)
        if len(adjacentNums) == 2:
            return prod(adjacentNums)
    return 0


def sumGearRatios(inputFileName: str) -> int:
    """Reads in file input and sums all part numbers"""
    with open(inputFileName, "r") as file:
        # convert input of strings to a 2D grid
        grid = [list(line) for line in file.read().splitlines()]
        gearRatios = [getGearRatio(row, col, grid) for row in range(
            len(grid)) for col in range(len(grid[row]))]
        return sum(gearRatios)


# Test case
assert (sumGearRatios("tests/1.txt") == 467835)

print("Part 2:", sumGearRatios("input.txt"))
