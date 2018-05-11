def getInputPhrase():
    return input("Enter your phrase: ").lower()

def getTotalOccurrencesOfLettersToCount( phrase, lettersToCount ):
    totalOccurrences = 0
    for character in phrase:
        if character in lettersToCount:
            totalOccurrences = totalOccurrences +1
    return totalOccurrences

def main():
    print("This program counts the number of given letters in an input phrase.")
    
    lettersToCount = input("Enter the letters to count in the phrase (e.g., 'aeiou'): ").lower()
    inputPhrase = getInputPhrase()

    totalOccurrencesOfLettersToCount = getTotalOccurrencesOfLettersToCount( phrase, lettersToCount )

    print("Total occurences of '{}' in your phrase: {}".format( lettersToCount, totalOccurrencesOfLettersToCount))

if __name__ == "__main__":
    main()
