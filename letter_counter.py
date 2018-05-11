def main():
    print("This program counts the number of given letters in an input phrase.")
    
    lettersToCount = input("Enter the letters to count in the phrase (e.g., 'aeiou'): ").lower()
    inputPhrase = input("Enter your phrase: ").lower()

    totalOccurrencesOfLettersToCount = 0
    for character in inputPhrase:
        if character in lettersToCount:
            totalOccurrencesOfLettersToCount = totalOccurrencesOfLettersToCount + 1

    print("Total occurences of '{}' in your phrase: {}".format( lettersToCount, totalOccurrencesOfLettersToCount))

if __name__ == "__main__":
    main()
