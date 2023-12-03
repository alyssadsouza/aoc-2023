from math import prod

############# Part 2 #############


def getMinCubeCount(sets: list[dict[str, int]]) -> dict[str, int]:
    """Determines the minimum cube count required for all the sets in the game to be valid"""
    minRed = max([set.get("red", 0) for set in sets])
    minGreen = max([set.get("green", 0) for set in sets])
    minBlue = max([set.get("blue", 0) for set in sets])
    return {"red": minRed, "green": minGreen, "blue": minBlue}


def getCubeCounts(set: str) -> dict[str, int]:
    """Returns count of each coloured cube in a set"""
    cubeCountsList = set.split(", ")
    cubeCounts = {colour: int(num) for cubeCount in cubeCountsList for num, colour in [cubeCount.split(" ")]}
    return cubeCounts


def getMinCubeSetPower(game: str) -> int:
    """Calculates the power of the minimum cube set"""
    sets = game.split(": ")[1].split("; ")
    minCubeCounts = getMinCubeCount([getCubeCounts(set) for set in sets])
    return prod(minCubeCounts.values())


def sumGamesMinCubeSetPowers(inputFileName: str) -> int:
    """Reads in file input and sums the minimum cube set power of each game"""
    with open(inputFileName, "r") as file:
        powers = [getMinCubeSetPower(game) for game in file.read().splitlines()]
        return sum(powers)


# Test case
assert (sumGamesMinCubeSetPowers("tests/1.txt") == 2286)

# Other tests
assert (getCubeCounts("3 blue, 4 red") == {"blue": 3, "red": 4})
assert (getCubeCounts("8 green, 6 blue, 20 red") == {"green": 8, "blue": 6, "red": 20})

assert (getMinCubeCount([{"blue": 3, "red": 4},{"red": 1, "green": 2, "blue": 6},{"green": 2}]) == {"red": 4, "green": 2, "blue": 6})
assert (getMinCubeCount([{"blue": 1, "green": 2}, {"green": 3, "blue": 4, "red": 1},{"green": 1, "blue": 1}]) == {"red": 1, "green": 3, "blue": 4})

assert (getMinCubeSetPower("Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green") == 48)
assert (getMinCubeSetPower("Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue") == 12)
assert (getMinCubeSetPower("Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red") == 1560)
assert (getMinCubeSetPower("Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red") == 630)
assert (getMinCubeSetPower("Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green") == 36)

print("Part 2:", sumGamesMinCubeSetPowers("input.txt"))
