def getInputPhrase():
    return input("Enter your phrase: ").lower()

def getVowelCount( phrase ):
    vowelCount = 0
    for character in phrase:
        if character in ['a','e','i','o','u']:
            vowelCount = vowelCount +1
    return vowelCount

def main():
    print("This program counts the number of vowels in an input phrase.")
    inputPhrase = getInputPhrase()

    totalVowels = getVowelCount( inputPhrase )

    print("Total vowels in your phrase: {}".format( totalVowels))

if __name__ == "__main__":
    main()
