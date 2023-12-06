############# Part 2 #############


def getNumberOfMatches(card: str) -> int:
    """Calculates card points"""
    winningNumbersString, myNumbersString = card.split(": ")[1].split(" | ")
    winningNumbers, myNumbers = winningNumbersString.split(), myNumbersString.split()
    matching = [1 if num in winningNumbers else 0 for num in myNumbers]
    return sum(matching) 


def sumCards(inputFileName: str) -> int:
    """Reads in file input and sums all card points"""
    with open(inputFileName, "r") as file:
        cards = [line for line in file.read().splitlines()]
        cardCount = [1 for card in cards] # counts the number of instances of each card in cards at the corresponding index
        for i in range(len(cards)):
            matches = getNumberOfMatches(cards[i])
            for j in range(i + 1, i + matches + 1):
                # for each instance of the current card, there is one extra copy of cards[j]
                cardCount[j] += cardCount[i]
        return sum(cardCount)


# Test case
assert (sumCards("tests/1.txt") == 30)

print("Part 2:", sumCards("input.txt"))
