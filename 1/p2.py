import re

############# Part 2 #############

numbers = {"one": "1", "two": "2", "three": "3", "four": "4",
           "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}


def suffix(input: str):
    """Returns a generator that yields the suffix of a string growing one char at a time"""
    return (input[-i-1:] for i in range(len(input)))


def getCalibrationValue(input: str) -> int:
    """Calculates calibration value for a string"""
    pattern = re.compile('\d|' + '|'.join(numbers.keys()))

    firstMatch = pattern.search(input).group(0)
    first = numbers.get(firstMatch, firstMatch)

    # check from end of input in case of strings like 'twone'
    inputSuffixGenerator, inputSuffix = suffix(input), ""
    while not pattern.search(inputSuffix):
        inputSuffix = next(inputSuffixGenerator)

    lastMatch = pattern.search(inputSuffix).group(0)
    last = numbers.get(lastMatch, lastMatch)

    return int(first + last)


def sumCalibrations(inputFileName: str) -> int:
    """Reads in file input and sums over each line's calibration value"""
    with open(inputFileName, "r") as file:
        calibrations = (getCalibrationValue(line) for line in file.readlines())
        return sum(calibrations)


# Test case
assert (sumCalibrations("tests/2.txt") == 281)

# Other tests
assert (getCalibrationValue("two1nine") == 29)
assert (getCalibrationValue("1asdas1") == 11)
assert (getCalibrationValue("eightwothree") == 83)
assert (getCalibrationValue("abcone2threexyz") == 13)
assert (getCalibrationValue("1ds3a223sda4s") == 14)
assert (getCalibrationValue("xtwone3four") == 24)
assert (getCalibrationValue("4nineeightseven2") == 42)
assert (getCalibrationValue("zoneight234") == 14)
assert (getCalibrationValue("7pqrstsixteen") == 76)
assert (getCalibrationValue("oneight") == 18)
assert (getCalibrationValue("twone") == 21)

print("Part 2:", sumCalibrations("input.txt"))
