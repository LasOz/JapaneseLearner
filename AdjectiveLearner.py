import csv
import random
import AdjectiveConjugator as AC

def Setup():
    adjectiveList = []
    with open('adjectivelist.csv', mode='r', encoding="utf8") as verbFile:
        verbReader = csv.DictReader(verbFile)
        for row in verbReader:
            adjectiveList.append(row)
    return adjectiveList

if __name__ == "__main__":
    adjectiveList = Setup()
    print("Beginning adjective trainer...")
    random.shuffle(adjectiveList)
    for adjective in adjectiveList:
        answer = input(f"What is {adjective['japanese']} ({adjective['furigana']}) the adjective for?\n")
        if (adjective['english'].count(answer) > 0):
            print(f"Correct. {adjective['japanese']} is a {adjective['type']}-adjective for '{adjective['english']}'")
            print(f"The Positive Present tense: {AC.Conjugate(adjective, False, True)}")
            print(f"The Negative Present tense: {AC.Conjugate(adjective, False, False)}")
            print(f"The Positive Past tense: {AC.Conjugate(adjective, True, True)}")
            print(f"The Negative Past tense: {AC.Conjugate(adjective, True, False)}")
        else:
            print(f"Oops, that wasn't right. {adjective['japanese']} ({adjective['furigana']}) is {adjective['english']}")
        print("Up next...")