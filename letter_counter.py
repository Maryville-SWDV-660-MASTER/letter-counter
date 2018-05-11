def main():
    print("This program counts the number of vowels in an input phrase.")
    inputPhrase = input("Enter your phrase: ").lower()

    totalVowels = 0
    for character in inputPhrase:
        if character in ['a','e','i','o','u']:
            totalVowels = totalVowels +1

    print("Total vowels in your phrase: {}".format( totalVowels))

if __name__ == "__main__":
    main()
