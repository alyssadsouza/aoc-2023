############# Part 1 #############

bagCounts = {"red": 12, "green": 13, "blue": 14}


def isPossibleSet(cubeCounts: dict[str, int]) -> bool:
    """Determines if all cube counts are valid in the set"""
    return not any(cubeCounts[colour] > bagCounts[colour] for colour in cubeCounts.keys())


def getCubeCounts(set: str) -> dict[str, int]:
    """Returns count of each coloured cube in a set"""
    cubeCountsList = set.split(", ")
    cubeCounts = {colour: int(num) for cubeCount in cubeCountsList for num, colour in [cubeCount.split(" ")]}
    return cubeCounts


def getIdIfPossibleGame(game: str) -> int:
    """Returns ID if possible game, else 0"""
    gameId, sets = game.split(": ")
    id = int(gameId.split(" ")[1])

    for set in sets.split("; "):
        if not isPossibleSet(getCubeCounts(set)):
            return 0

    return id


def sumPossibleGameIDs(inputFileName: str) -> int:
    """Reads in file input and sums IDs of each possible game"""
    with open(inputFileName, "r") as file:
        possibleIDs = [getIdIfPossibleGame(game) for game in file.read().splitlines()]
        return sum(possibleIDs)


# Test case
assert (sumPossibleGameIDs("tests/1.txt") == 8)

# Other tests
assert (getCubeCounts("3 blue, 4 red") == {"blue": 3, "red": 4})
assert (getCubeCounts("8 green, 6 blue, 20 red") == {"green": 8, "blue": 6, "red": 20})

assert (isPossibleSet({"blue": 3, "red": 4}) == True)
assert (isPossibleSet({"green": 8, "blue": 6, "red": 20}) == False)

assert (getIdIfPossibleGame("Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green") == 1)
assert (getIdIfPossibleGame("Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue") == 2)
assert (getIdIfPossibleGame("Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red") == 0)

print("Part 1:", sumPossibleGameIDs("input.txt"))
