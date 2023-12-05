############# Part 1 #############


def isSymbol(input: str) -> bool:
    """Determines if a string in the schematic is a symbol"""
    return input != "." and not input.isdigit()


def isAdjacentToSymbol(row: int, col: int, grid: list[list]) -> bool:
    """Determines if an element at this given row and column is adjacent to a symbol"""
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
    for pos in adjacentPositions:
        y, x = pos
        if 0 <= y < len(grid) and 0 <= x < len(grid[y]) and isSymbol(grid[y][x]):
            return True

    return False


def getNumberFromDigitAtPos(row: int, col: int, grid: list[list]) -> tuple[int, int]:
    """
    Returns whole number from schematics given a single digit at specified position
    Also returns updated column to continue on from
    """
    num = ""
    # get to the start of the number (leftmost digit)
    while col - 1 >= 0 and grid[row][col - 1].isdigit():
        col -= 1
    # get each digit one at a time left to right
    while col < len(grid[row]) and grid[row][col].isdigit():
        num += grid[row][col]
        col += 1

    return (int(num), col)


def sumPartNumbers(inputFileName: str) -> int:
    """Reads in file input and sums all part numbers"""
    with open(inputFileName, "r") as file:
        # convert input of strings to a 2D grid
        grid = [list(line) for line in file.read().splitlines()]

        partNumbers = 0
        row, col = 0, 0

        while row < len(grid):
            while col < len(grid[row]):
                # if a digit is adjacent to symbol, add the whole number to sum and move past whole number
                if grid[row][col].isdigit() and isAdjacentToSymbol(row, col, grid):
                    partNumber, col = getNumberFromDigitAtPos(row, col, grid)
                    partNumbers += partNumber

                else:
                    col += 1

            row, col = row + 1, 0

        return partNumbers


# Test case
assert (sumPartNumbers("tests/1.txt") == 4361)

print("Part 1:", sumPartNumbers("input.txt"))
