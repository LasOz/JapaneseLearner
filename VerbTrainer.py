import csv
import os
import random
import VerbConjugator as VC
import time
import window as GW
from threading import Thread

class VerbTrainer:
    verbList = []
    verbIndex = -1

    def __init__(self):
        verbList = self.Setup()
        random.shuffle(verbList)

    def Setup(self):
        print("Beginning verb trainer...")
        with open('verblist.csv', mode='r', encoding="utf8") as verbFile:
            verbReader = csv.DictReader(verbFile)
            for row in verbReader:
                self.verbList.append(row)
        return self.verbList

    def train(self):
        for self.verbIndex, verb in enumerate(self.verbList):
            GW.play_sound(os.path.join("VerbClips", f"{verb['english'].replace(' ','_')}.mp3"))
            answer = input(f"What is {verb['japanese']} ({verb['furigana']}) the verb for?\n")
            if (verb['english'].count(answer) > 0):
                print(f"Correct. {verb['japanese']} is a {verb['verb-type']}-verb for '{verb['english']}'")
                print(f"The Polite Present Indicative tense: {VC.Conjugate(verb, 'present', True)}")
                print(f"The Plain Present Indicative tense: {VC.Conjugate(verb, 'present', False)}")
                print(f"The Polite Past Indicative tense: {VC.Conjugate(verb, 'past', True)}")
                print(f"The Plain Past Indicative tense: {VC.Conjugate(verb, 'past', False)}")
                print(f"The te-form: {VC.TeForm(verb)}")
            else:
                print(f"Oops, that wasn't right. {verb['japanese']} ({verb['furigana']}) is {verb['english']}")

    def next_word(self):
        print("Beginning verb trainer...")
        if (self.verbIndex < len(self.verbList)):
            self.verbIndex += 1
            return True
        else:
            return False

if __name__ == "__main__":
    VT = VerbTrainer()
    with GW.game_window(500,500) as window:
        a = Thread(target = VT.train)
        a.start()
        while (not window.was_closed()) and a.is_alive():
            path = os.path.join("VerbPictures", f"{VT.verbList[VT.verbIndex]['english']}")
            image = GW.load_image(path.replace(' ','_'))
            image = GW.scale_screen(image)
            window.screen.blit(image, (0,0))
            GW.write_on_screen(window.screen, VT.verbList[VT.verbIndex]['furigana'], (0,0))
            GW.write_on_screen(window.screen, VT.verbList[VT.verbIndex]['japanese'], (0,50))
            window.flip()
        exit()