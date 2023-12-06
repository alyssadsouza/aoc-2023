############# Part 1 #############


def getCardPoints(card: str) -> int:
    """Calculates card points"""
    winningNumbersString, myNumbersString = card.split(": ")[1].split(" | ")
    winningNumbers, myNumbers = winningNumbersString.split(), myNumbersString.split()
    points = [1 if num in winningNumbers else 0 for num in myNumbers]
    return 2 ** (sum(points) - 1) if 1 in points else 0


def sumCardPoints(inputFileName: str) -> int:
    """Reads in file input and sums all card points"""
    with open(inputFileName, "r") as file:
        cards = [line for line in file.read().splitlines()]
        points = [getCardPoints(card) for card in cards]

        return sum(points)


# Test case
assert (sumCardPoints("tests/1.txt") == 13)

print("Part 1:", sumCardPoints("input.txt"))
