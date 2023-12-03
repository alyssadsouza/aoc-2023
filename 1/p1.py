import re

############# Part 1 #############


def getCalibrationValue(input: str) -> int:
    """Calculates calibration value for a string"""
    pattern = re.compile(r'\d')
    first = pattern.search(input).group(0) # get first digit in string
    last = pattern.search(input[::-1]).group(0) # get last digit by iterating in reverse
    return int(first + last)


def sumCalibrations(inputFileName: str) -> int:
    """Reads in file input and sums over each line's calibration value"""
    with open(inputFileName, "r") as file:
        calibrations = [getCalibrationValue(line) for line in file.readlines()]
        return sum(calibrations)


# Test case
assert (sumCalibrations("tests/1.txt") == 142)

# Other tests
assert (getCalibrationValue("asdas1") == 11)
assert (getCalibrationValue("1asdas1") == 11)
assert (getCalibrationValue("dsa2sda3s") == 23)
assert (getCalibrationValue("dsa22sdas") == 22)
assert (getCalibrationValue("1ds3a223sda4s") == 14)

print("Part 1:", sumCalibrations("input.txt"))
