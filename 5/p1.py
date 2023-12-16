############# Part 1 #############

def formatAlmanacData(input: list[str]) -> tuple[list, list]:
    """
    Pulls out string inputs separating the seeds from maps and formatting for easy use
	- seeds: `list[ints]`
    - maps: `list[{ 'destination-start': int, 'source-start': int, 'range': int }]`
    """
    seeds = [int(seed) for seed in input[0].split()[1:]]
    maps = [[{'destination-start': int(map.split()[0]), 'source-start': int(map.split()[1]), 'range': int(
        map.split()[2])} for map in line.strip().split("\n")[1:]] for line in input[1:]]
    return (seeds, maps)


def getNextNum(currentNum: int, map: list) -> int:
    """Gets next number in the mapping"""
    for mapping in map:
        if mapping['source-start'] <= currentNum <= mapping['source-start'] + mapping['range']:
            return mapping['destination-start'] + (currentNum - mapping['source-start'])
    return currentNum


def getLocationNumber(seed: int, maps: list) -> int:
    """Calculates location number given seed using almanac mapping"""
    currentNum = seed
    for map in maps:
        currentNum = getNextNum(currentNum, map)
    return currentNum


def findLowestLocationNumber(inputFileName: str) -> int:
    """Reads in file input and finds lowest location number"""
    with open(inputFileName, "r") as file:
        input = [line for line in file.read().split("\n\n")]
        seeds, maps = formatAlmanacData(input)
        locationNums = [getLocationNumber(seed, maps) for seed in seeds]
        return min(locationNums)


# Test case
assert (findLowestLocationNumber("tests/1.txt") == 35)

print("Part 1:", findLowestLocationNumber("input.txt"))
