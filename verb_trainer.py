"""The verb trainer class and game loop"""

import csv
import random
import os
from threading import Thread
import romkan
import verb_conjugator as VC
import window as graphics
import typer as keyboard
import event_handler as EH

class VerbTrainer:
    """The class for handling the verb trainer game logic"""
    verb_list = []
    verb_index = -1
    m_finished = False

    def __init__(self):
        self.verb_list = self.setup()
        random.shuffle(self.verb_list)

    def setup(self):
        """Setup the game by reading the csv file"""
        print("Beginning verb trainer...")
        with open('verblist.csv', mode='r', encoding="utf8") as verb_file:
            verb_reader = csv.DictReader(verb_file)
            for row in verb_reader:
                self.verb_list.append(row)
        return self.verb_list

    def train(self):
        """The training loop"""
        for self.verb_index, verb in enumerate(self.verb_list):
            graphics.play_sound(os.path.join("VerbClips",
                                             f"{verb['english'].replace(' ','_')}.mp3"))
            answer = input(f"What is {verb['japanese']} ({verb['furigana']}) the verb for?\n")
            if verb['english'].count(answer) > 0:
                print(f"Correct. {verb['japanese']} is a "+
                      f"{verb['verb-type']}-verb for '{verb['english']}'")
                print(f"The Polite Present Indicative tense: {VC.conjugate(verb, 'present', True)}")
                print(f"The Plain Present Indicative tense: {VC.conjugate(verb, 'present', False)}")
                print(f"The Polite Past Indicative tense: {VC.conjugate(verb, 'past', True)}")
                print(f"The Plain Past Indicative tense: {VC.conjugate(verb, 'past', False)}")
                print(f"The te-form: {VC.te_form(verb)}")
            else:
                print("Oops, that wasn't right. " +
                      f"{verb['japanese']} ({verb['furigana']}) is {verb['english']}")
        self.m_finished = True

    def next_word(self):
        """Advance the game to the next word"""
        print("Beginning verb trainer...")
        if self.verb_index < len(self.verb_list):
            self.verb_index += 1
            return True
        return False

    def current_picture(self):
        """Get the current image of the game sequence"""
        if self.verb_list:
            file_name = f"{self.verb_list[self.verb_index]['english']}.jpg"
            return os.path.join("VerbPictures", file_name).replace(' ', '_')
        return os.path.join("VerbPictures", "Loading.jpg")

def game_loop():
    """It's just the game loop"""
    verb_trainer = VerbTrainer()
    clock = graphics.get_clock()
    with graphics.GameWindow(500, 500) as window:
        verb_trainer_thread = Thread(target=verb_trainer.train)
        verb_trainer_thread.start()
        typer = keyboard.Typer()
        event_handler = EH.EventHandler()
        event_handler.add_to_listen(window.was_closed)
        event_handler.add_to_listen(typer.get_keystrokes)
        while (not window.closed) and (not verb_trainer.m_finished):
            event_handler.check_events()
            image = graphics.load_image(verb_trainer.current_picture())
            window.blit_to_scale(image, (0, 0))
            graphics.write_on_screen(window.screen,
                                     verb_trainer.verb_list[verb_trainer.verb_index]['furigana'],
                                     (0, 0))
            graphics.write_on_screen(window.screen,
                                     verb_trainer.verb_list[verb_trainer.verb_index]['japanese'],
                                     (0, 50))
            graphics.write_on_screen(window.screen, romkan.to_hiragana(typer.m_text), (0, 100))
            window.flip()
            clock.tick(30)
        exit()

if __name__ == "__main__":
    game_loop()
